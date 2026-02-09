r"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |           FalconPy
`-------'                         `-------'

This sample utilizes the Exposure Management service collection
to identify exposed assets and return the results as a PDF report.


USAGE EXAMPLES:
    # Generate PDF report with default settings
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET

    # Generate dark mode PDF with custom filename
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET -o my_report.pdf --dark

    # Export to JSON format
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET -f json -o report.json

    # Export to CSV format
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET -f csv -o report.csv

    # Filter by specific subsidiary
    python3 em_manager.py -k $EASM_KEY -s $EASM_SECRET --subsidiary "Company Name"

Creation date: 12.10.25 - alhumaw
"""

import csv
import json
import logging
import os
from datetime import datetime
from dataclasses import dataclass, asdict
from operator import attrgetter
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
try:
    from falconpy import ExposureManagement, APIError
except ImportError as no_falconpy:
    raise SystemExit("The CrowdStrike FalconPy library must be installed.\n"
                     "Install it with `python3 -m pip install crowdstrike-falconpy`."
                     ) from no_falconpy
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.platypus import (
        SimpleDocTemplate, Table,
        TableStyle, Paragraph,
        Spacer, PageBreak,
        PageTemplate, Frame, 
        Image
        )
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
except ImportError as no_reportlab:
    raise SystemExit("The reportlab library must be installed.\n"
                     "Install it with `python3 -m pip install reportlab`."
                     ) from no_reportlab

# query_external_assets using filter for critical and high
@dataclass
class ImportantAsset:
    criticality: str
    asset_type: str
    ip_address: str
    fqdn: str
    confidence: int
    status: str
    location: dict
    internet_exposure: str = None
    perimeter: str = None
    isp: str = None
    asn: int = None
    country_name: str = None
    triage_status: str = None
    triage_action: str = None
    discovered_by: str = None

# aggregate_external_assets()
@dataclass
class Application:
    name: str
    count: int

# aggregate_external_assets()
@dataclass
class AssetSummary:
    total_assets: int = None
    critical: int = None
    high: int = None
    noncritical: int = None
    unassigned: int = None

# query_ecosystem_subsidiaries()
@dataclass
class Subsidiary:
    id: str
    name: str
    primary_domain: str

@dataclass
class EnhancedStats:
    total_assets: int = 0
    internet_exposed: int = 0
    shadow_it: int = 0
    triaged: int = 0
    online: int = 0
    offline: int = 0
    auto_discovered: int = 0
    manual_discovered: int = 0
    countries: dict = None
    isps: dict = None

    def __post_init__(self):
        if self.countries is None:
            self.countries = {}
        if self.isps is None:
            self.isps = {}

@dataclass
class DiscoveryPath:
    asset_id: str
    asset_fqdn: str
    path_steps: list
    criticality: str

@dataclass
class AggregateResults:
    name: str
    subsidiary: Subsidiary
    asset_summary: AssetSummary
    applications: list[Application]
    important_assets: list[ImportantAsset]
    enhanced_stats: EnhancedStats = None
    discovery_paths: list[DiscoveryPath] = None

    def __post_init__(self):
        if self.enhanced_stats is None:
            self.enhanced_stats = EnhancedStats()
        if self.discovery_paths is None:
            self.discovery_paths = []

def parse_command_line() -> Namespace:
    """Parse any provided command line arguments and return the namespace."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)

    require = parser.add_argument_group("required arguments")
    require.add_argument("-k", "--client_id", required=True, help="CrowdStrike API client ID")
    require.add_argument("-s", "--client_secret", required=True, help="CrowdStrike API client secret")

    parser.add_argument("-d", "--debug", help="Enable API debugging", action="store_true", default=False)
    parser.add_argument("-o", "--output", help="Output filename (default: Executive_Report.pdf)",
                       default="Executive_Report.pdf")
    parser.add_argument("-f", "--format", help="Export format: pdf, json, csv (default: pdf)",
                       choices=['pdf', 'json', 'csv'], default='pdf')
    parser.add_argument("--dark", help="Enable dark mode for PDF reports", action="store_true", default=False)
    parser.add_argument("--subsidiary", help="Filter by specific subsidiary name", default=None)
    parser.add_argument("--logo", help="Path to logo image for PDF reports (default: img/cs-logo.png)",
                       default="img/cs-logo.png")

    parsed = parser.parse_args()

    if parsed.debug:
        logging.basicConfig(level=logging.DEBUG)

    if parsed.format != 'pdf' and parsed.dark:
        parser.error("--dark can only be used with PDF format")

    return parsed

class ExposureManagementReport:
    def __init__(self, file_name: str, aggregated_results: list[AggregateResults], dark_mode: bool = False, logo_path: str = "img/cs-logo.png"):
        self.aggregated_results = aggregated_results
        self.file_name = file_name
        self.dark_mode = dark_mode
        self.logo_path = logo_path
        self.has_logo = os.path.isfile(logo_path)

        if not self.has_logo:
            print(f"Warning: Logo file not found at '{logo_path}'. Report will be generated without logo.")

        self.doc = SimpleDocTemplate(file_name, pagesize=A4,
                                      rightMargin=0.75*inch, leftMargin=0.75*inch,
                                      topMargin=1*inch, bottomMargin=0.75*inch, )
        self.story = []
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

        if self.dark_mode:
            self._setup_dark_mode_template()

    def _draw_dark_background(self, canvas, doc):
        """Draw black background on each page"""
        canvas.saveState()
        canvas.setFillColor(colors.black)
        canvas.rect(0, 0, A4[0], A4[1], fill=True, stroke=False)
        canvas.restoreState()

    def _setup_dark_mode_template(self):
        """Setup page template with black background"""
        frame = Frame(
            self.doc.leftMargin,
            self.doc.bottomMargin,
            self.doc.width,
            self.doc.height,
            id='normal'
        )
        template = PageTemplate(
            id='DarkMode',
            frames=[frame],
            onPage=self._draw_dark_background
        )
        self.doc.addPageTemplates([template])

    def _truncate_fqdn(self, fqdn: str, max_length: int = 40) -> str:
        """Truncate FQDN if it exceeds max length.

        Parameters:
            fqdn -- The FQDN to potentially truncate.
            max_length -- Maximum character length before truncation.

        Returns: Truncated FQDN with ellipsis if needed.
        """
        if not fqdn or fqdn == 'N/A':
            return fqdn
        if len(fqdn) <= max_length:
            return fqdn
        return fqdn[:max_length-3] + '...'

    def _setup_custom_styles(self):
        """Setup custom styles following CrowdStrike Brand Identity."""
        CRWD_RED = colors.HexColor('#EC0000')
        CRWD_BLACK = colors.HexColor('#000000')
        CRWD_WHITE = colors.HexColor('#FFFFFF')
        CRWD_CLOUD = colors.HexColor('#F8F8F8')
        CRWD_DEEP_SEA = colors.HexColor('#3D474F')
        CRWD_SURF = colors.HexColor('#61C4C9')

        if self.dark_mode:
            title_color = CRWD_WHITE
            heading_color = CRWD_RED
            body_color = CRWD_CLOUD
            footer_color = CRWD_CLOUD
        else:
            title_color = CRWD_RED
            heading_color = CRWD_RED
            body_color = CRWD_BLACK
            footer_color = CRWD_DEEP_SEA

        self.title_style = ParagraphStyle(
            'ReportTitle',
            parent=self.styles['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=20,
            alignment=TA_CENTER,
            textColor=title_color,
            spaceAfter=20
        )

        self.heading_style = ParagraphStyle(
            'SectionHeading',
            parent=self.styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=14,
            spaceBefore=16,
            spaceAfter=8,
            textColor=heading_color
        )

        self.subheading_style = ParagraphStyle(
            'SubHeading',
            parent=self.styles['Heading3'],
            fontName='Helvetica-Bold',
            fontSize=12,
            spaceBefore=12,
            spaceAfter=6,
            textColor=title_color,
            alignment=TA_CENTER
        )

        self.meta_style = ParagraphStyle(
            'CustomBody',
            parent=self.styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            leading=14,
            alignment=TA_CENTER,
            textColor=body_color
        )

        self.body_style = ParagraphStyle(
            'CustomBody',
            parent=self.styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            leading=14,
            alignment=TA_LEFT,
            textColor=body_color
        )

        self.footer_style = ParagraphStyle(
            'Footer',
            parent=self.styles['Normal'],
            fontName='Helvetica',
            fontSize=8,
            textColor=footer_color,
            alignment=TA_CENTER
        )

    def add_title(self, title_text):
        """Add main report title using Sans Bold"""
        if self.has_logo:
            try:
                self.story.append(Image(self.logo_path, width=inch * 5, height=inch * 1, hAlign=TA_CENTER))
                self.story.append(Spacer(1, 0.2*inch))
            except Exception as e:
                print(f"Warning: Failed to load logo image: {e}")
        self.story.append(Paragraph(title_text, self.title_style))
        self.story.append(Spacer(1, 0.2*inch))

    def add_metadata(self):
        """Add report metadata (date, summary stats)"""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        metadata = f"<b>{timestamp}</b><br/>"

        self.story.append(Paragraph(metadata, self.meta_style))
        self.story.append(Spacer(1, 0.3*inch))

    def add_section(self, heading_text):
        """Add a section heading using Sans Bold"""
        self.story.append(Paragraph(heading_text, self.heading_style))

    def add_subsection(self, subheading_text):
        """Add a subsection heading using Sans Bold"""
        self.story.append(Paragraph(subheading_text, self.subheading_style))

    def add_paragraph(self, text):
        """Add body paragraph"""
        self.story.append(Paragraph(text, self.body_style))
        self.story.append(Spacer(1, 0.1*inch))

    def _split_applications_into_columns(self, applications, num_columns=2):
        """Split applications list into multi-column table format for compact display"""
        if not applications:
            return [['Application Name', 'Count'] * num_columns]
        
        rows_per_column = (len(applications) + num_columns - 1) // num_columns
        
        headers = ['Application Name', 'Count'] * num_columns
        table_data = [headers]
        
        for row_idx in range(rows_per_column):
            row = []
            for col_idx in range(num_columns):
                data_idx = col_idx * rows_per_column + row_idx
                if data_idx < len(applications):
                    app = applications[data_idx]
                    row.extend([app.name, str(app.count)])
                else:
                    row.extend(['', ''])
            table_data.append(row)
        
        return table_data

    def add_executive_summary(self):
        """Add executive summary section"""
        self.add_section("Executive Summary")
        total = 0
        critical = 0
        for result in self.aggregated_results:
            if result.asset_summary.total_assets:
                total += result.asset_summary.total_assets
            if result.asset_summary.critical:
                critical += result.asset_summary.critical
        
        summary = f"""This report identifies <b>{total}</b> exposed assets within your attack surface. 
        Of these, <b>{critical}</b> are classified as <b>Critical Risk</b> requiring immediate attention. 
        Exposed assets represent potential entry points for attackers and should be remediated 
        according to their risk classification."""
        
        self.add_paragraph(summary)
        self.story.append(Spacer(1, 0.2*inch))
    
    def add_understanding_section(self):
        """Add section explaining Falcon EASM concepts"""
        self.add_section("Understanding Your External Attack Surface")
        
        intro = """Falcon EASM constructs your digital footprint by indexing the internet and discovering 
        your known and unknown internet-facing assets. This section explains key concepts used in this report."""
        self.add_paragraph(intro)
        
        # Subsidiaries
        self.add_subsection("Subsidiaries and Organizational Structure")
        subsidiary_text = """An organization's external attack surface may include multiple subsidiaries, 
        representing different business units, acquired companies, or regional operations. This report organizes 
        assets by subsidiary to provide clear visibility into each entity's security posture:<br/><br/>
        Your organization may be a single root subsidiary, 
        or you may represent it as multiple subsidiaries, with varying levels of nesting, under a single root.
        """
        self.add_paragraph(subsidiary_text)
        
        # Criticality Levels
        self.add_subsection("Criticality Classifications")
        criticality_text = """Assets are classified by business impact and risk level:<br/><br/>
        <b>Critical</b> - Assets requiring immediate attention due to severe security risk.<br/>
        <b>High</b> - Assets with significant security concerns that should be prioritized.<br/>
        <b>Noncritical</b> - Assets with lower risk profiles or less business impact.<br/>
        <b>Unassigned</b> - Assets that have not yet been assigned a criticality level."""
        self.add_paragraph(criticality_text)
        
        self.story.append(PageBreak())
    
    def add_subsidiary_section(self):

        for result in self.aggregated_results:
            critical = 0
            high = 0
            noncritical = 0
            unassigned = 0
            total = 0
            self.add_section(f"{result.name}")
            if result.asset_summary.critical:
                critical = result.asset_summary.critical
            if result.asset_summary.high:
                high = result.asset_summary.high
            if result.asset_summary.noncritical:
                noncritical = result.asset_summary.noncritical
            if result.asset_summary.unassigned:
                unassigned = result.asset_summary.unassigned
            if result.asset_summary.total_assets:
                total = result.asset_summary.total_assets
            self.add_subsection("Exposed Assets Summary")
            summary_data = [
                ['Critical', 'High', 'Noncritical', 'Unassigned', 'Total'],
                [str(critical), str(high), str(noncritical), str(unassigned), str(total)]
            ]
            CRWD_DEEP_SEA = colors.HexColor('#3D474F')
            CRWD_CLOUD = colors.HexColor('#F8F8F8')
            summary_table = Table(summary_data, colWidths=[1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch])
            summary_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), CRWD_DEEP_SEA),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 9),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, CRWD_CLOUD]),
                ('GRID', (0, 0), (-1, -1), 0.5, CRWD_DEEP_SEA),
                ('BOX', (0, 0), (-1, -1), 1.5, CRWD_DEEP_SEA),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ]))

            self.story.append(summary_table)
            self.story.append(Spacer(1, 0.3*inch))

            # Applications Table
            if result.applications:
                self.add_subsection("Exposed Applications")
                
                # Use multi-column layout if more than 10 applications
                num_cols = 2 if len(result.applications) > 5 else 1
                
                if num_cols == 1:
                    app_data = [['Application Name', 'Count']]
                    for app in result.applications:
                        app_data.append([app.name, str(app.count)])
                    col_widths = [4*inch, 1.2*inch]
                else:
                    app_data = self._split_applications_into_columns(result.applications, num_cols)
                    col_widths = [2*inch, 0.8*inch, 2*inch, 0.8*inch]
                
                app_table = Table(app_data, colWidths=col_widths)
                app_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), CRWD_DEEP_SEA),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 9),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, CRWD_CLOUD]),
                    ('GRID', (0, 0), (-1, -1), 0.5, CRWD_DEEP_SEA),
                    ('BOX', (0, 0), (-1, -1), 1.5, CRWD_DEEP_SEA),
                    ('TOPPADDING', (0, 0), (-1, -1), 8),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ]))
                
                self.story.append(app_table)
                self.story.append(Spacer(1, 0.3*inch))
            
            # Important Assets Table
            if result.important_assets:
                self.add_subsection("Critical & High Risk Assets")
                
                asset_data = [['FQDN', 'IP', 'Asset Type', 'Criticality', 'Confidence', 'Status']]
                
                for asset in result.important_assets:
                    fqdn = self._truncate_fqdn(asset.fqdn if asset.fqdn else 'N/A', max_length=35)
                    ip = asset.ip_address if asset.ip_address else 'N/A'
                    asset_type = asset.asset_type if asset.asset_type else 'N/A'
                    criticality = asset.criticality if asset.criticality else 'N/A'
                    confidence = f"{asset.confidence}%" if asset.confidence else 'N/A'
                    status = asset.status if asset.status else 'N/A'

                    asset_data.append([fqdn, ip, asset_type, criticality, confidence, status])
                
                asset_table = Table(asset_data, colWidths=[2*inch, 2*inch, 1.2*inch, 1*inch, 0.8*inch, 0.8*inch])
                asset_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), CRWD_DEEP_SEA),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('ALIGN', (0, 1), (0, -1), 'LEFT'),
                    ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 9),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, CRWD_CLOUD]),
                    ('GRID', (0, 0), (-1, -1), 0.5, CRWD_DEEP_SEA),
                    ('BOX', (0, 0), (-1, -1), 1.5, CRWD_DEEP_SEA),
                    ('TOPPADDING', (0, 0), (-1, -1), 8),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ]))
                
                # Color-code criticality cells
                CRWD_RED = colors.HexColor('#EC0000')
                CRWD_ORANGE = colors.HexColor('#FF8C00')
                
                for i, asset in enumerate(result.important_assets, start=1):
                    if asset.criticality == 'Critical':
                        asset_table.setStyle(TableStyle([
                            ('BACKGROUND', (2, i), (2, i), CRWD_RED),
                            ('TEXTCOLOR', (2, i), (2, i), colors.white),
                            ('FONTNAME', (2, i), (2, i), 'Helvetica-Bold'),
                        ]))
                    elif asset.criticality == 'High':
                        asset_table.setStyle(TableStyle([
                            ('BACKGROUND', (2, i), (2, i), CRWD_ORANGE),
                            ('TEXTCOLOR', (2, i), (2, i), colors.white),
                            ('FONTNAME', (2, i), (2, i), 'Helvetica-Bold'),
                        ]))
                
                self.story.append(asset_table)
                self.story.append(Spacer(1, 0.3*inch))
            
            self.story.append(PageBreak())

    def add_enhanced_statistics_section(self):
        """Add enhanced statistics for all subsidiaries."""
        self.add_section("Enhanced Attack Surface Analysis")

        CRWD_DEEP_SEA = colors.HexColor('#3D474F')
        CRWD_CLOUD = colors.HexColor('#F8F8F8')

        for result in self.aggregated_results:
            if not result.enhanced_stats:
                continue

            stats = result.enhanced_stats
            self.add_subsection(f"{result.name} - Security Posture")

            self.add_paragraph(f"<b> Critical/High Internet Exposure:</b> {stats.internet_exposed} of {stats.total_assets} assets are publicly accessible")

            stats_data = [
                ['Metric', 'Count', 'Percentage'],
                ['Internet Exposed', str(stats.internet_exposed), f"{stats.internet_exposed/stats.total_assets*100:.1f}%" if stats.total_assets > 0 else 'N/A'],
                ['Shadow IT', str(stats.shadow_it), f"{stats.shadow_it/stats.total_assets*100:.1f}%" if stats.total_assets > 0 else 'N/A'],
                ['Triaged Assets', str(stats.triaged), f"{stats.triaged/stats.total_assets*100:.1f}%" if stats.total_assets > 0 else 'N/A'],
                ['Online', str(stats.online), f"{stats.online/stats.total_assets*100:.1f}%" if stats.total_assets > 0 else 'N/A'],
                ['Offline', str(stats.offline), f"{stats.offline/stats.total_assets*100:.1f}%" if stats.total_assets > 0 else 'N/A'],
                ['Auto-discovered', str(stats.auto_discovered), f"{stats.auto_discovered/stats.total_assets*100:.1f}%" if stats.total_assets > 0 else 'N/A'],
                ['Manually Added', str(stats.manual_discovered), f"{stats.manual_discovered/stats.total_assets*100:.1f}%" if stats.total_assets > 0 else 'N/A'],
            ]

            stats_table = Table(stats_data, colWidths=[3*inch, 1.5*inch, 2*inch])
            stats_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), CRWD_DEEP_SEA),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 9),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, CRWD_CLOUD]),
                ('GRID', (0, 0), (-1, -1), 0.5, CRWD_DEEP_SEA),
                ('BOX', (0, 0), (-1, -1), 1.5, CRWD_DEEP_SEA),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ]))

            self.story.append(stats_table)
            self.story.append(Spacer(1, 0.3*inch))

            if stats.countries:
                self.add_subsection("Geographic Distribution")
                sorted_countries = sorted(stats.countries.items(), key=lambda x: x[1], reverse=True)[:10]

                country_data = [['Country', 'Asset Count']]
                for country, count in sorted_countries:
                    country_data.append([country, str(count)])

                country_table = Table(country_data, colWidths=[4*inch, 2*inch])
                country_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), CRWD_DEEP_SEA),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 9),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, CRWD_CLOUD]),
                    ('GRID', (0, 0), (-1, -1), 0.5, CRWD_DEEP_SEA),
                    ('BOX', (0, 0), (-1, -1), 1.5, CRWD_DEEP_SEA),
                    ('TOPPADDING', (0, 0), (-1, -1), 8),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ]))

                self.story.append(country_table)
                self.story.append(Spacer(1, 0.3*inch))

            if stats.isps:
                self.add_subsection("Top Hosting Providers")
                sorted_isps = sorted(stats.isps.items(), key=lambda x: x[1], reverse=True)[:10]

                isp_data = [['Hosting Provider', 'Asset Count']]
                for isp, count in sorted_isps:
                    isp_data.append([isp if isp else 'Unknown', str(count)])

                isp_table = Table(isp_data, colWidths=[4*inch, 2*inch])
                isp_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), CRWD_DEEP_SEA),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 9),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, CRWD_CLOUD]),
                    ('GRID', (0, 0), (-1, -1), 0.5, CRWD_DEEP_SEA),
                    ('BOX', (0, 0), (-1, -1), 1.5, CRWD_DEEP_SEA),
                    ('TOPPADDING', (0, 0), (-1, -1), 8),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ]))

                self.story.append(isp_table)
                self.story.append(Spacer(1, 0.3*inch))

        self.story.append(PageBreak())

    def add_discovery_paths_section(self):
        """Add discovery path examples to show how assets were found."""
        self.add_section("Asset Discovery Intelligence")

        intro = """Understanding how assets were discovered helps identify shadow IT, third-party
        dependencies, and potential security gaps. Below are example discovery chains showing how
        Falcon EASM traced assets back to your organization."""
        self.add_paragraph(intro)

        for result in self.aggregated_results:
            if not result.discovery_paths:
                continue

            self.add_subsection(f"{result.name} - Discovery Examples")

            for idx, path in enumerate(result.discovery_paths[:5], 1):
                criticality_color = "red" if path.criticality == "Critical" else "orange"
                self.add_paragraph(f"<b>Discovery Chain {idx}:</b> {self._truncate_fqdn(path.asset_fqdn, 50)} "
                                 f"(<font color='{criticality_color}'><b>{path.criticality}</b></font>)")

                path_text = ""
                indent_base = 0

                for step_idx, step in enumerate(reversed(path.path_steps)):
                    entity = step.get('entity', 'Unknown')
                    entity_type = step.get('entity_type', 'unknown')
                    clue = step.get('clue', '')

                    indent = "&nbsp;" * (indent_base * 4)

                    path_text += f"{indent}<b>{entity}</b> <i>({entity_type})</i><br/>"

                    if clue and step_idx < len(path.path_steps) - 1:
                        truncated_clue = clue[:100] + "..." if len(clue) > 100 else clue
                        path_text += f"{indent}&nbsp;&nbsp;\u21b3 <i>{truncated_clue}</i><br/>"

                    if step_idx < len(path.path_steps) - 1:
                        path_text += f"{indent}&nbsp;&nbsp;&nbsp;&nbsp;\u2193<br/>"

                    indent_base += 1

                self.add_paragraph(path_text)
                self.story.append(Spacer(1, 0.2*inch))

        self.story.append(PageBreak())


    def build(self):
        """Build the complete PDF report"""
        try:
            self.add_title("Exposed Assets Security Report")
            self.add_metadata()
            self.add_executive_summary()
            self.add_understanding_section()
            self.add_enhanced_statistics_section()
            self.add_discovery_paths_section()
            self.add_subsidiary_section()

            self.story.append(Spacer(1, 0.5*inch))
            footer_text = "This report is confidential and intended for internal use only."
            self.story.append(Paragraph(footer_text, self.footer_style))

            if self.dark_mode:
                self.doc.build(
                    self.story,
                    onFirstPage=self._draw_dark_background,
                    onLaterPages=self._draw_dark_background
                    )
            else:
                self.doc.build(self.story)

            print(f"Report generated successfully: {self.file_name}")
        except Exception as e:
            raise SystemExit(f"Failed to generate PDF report: {e}") from e

class ExposedAssetsManager:
    """Manage exposure management data collection and aggregation."""
    def __init__(self, falcon: ExposureManagement, subsidiary_filter: str = None):
        self.falcon = falcon
        self.subsidiary_filter = subsidiary_filter
        self.raw_subsidiaries = []
        self.raw_asset_summary = []
        self.raw_applications = []
        self.raw_assets = {}
        self.no_subsidiaries = False

    def query_subsidiaries(self):
        print("\n[1/4] Querying subsidiaries...")
        response = self.falcon.query_combined_ecosystem_subsidiaries()
        code = response['status_code']
        if code != 200:
            raise SystemExit(f"Error querying subsidiaries. Status code: {code}\n"
                           f"Details: {response.get('body', {}).get('errors', 'Unknown error')}")

        body = response.get('body')
        resources = body.get('resources')
        if resources is None:
            print("  No subsidiaries found. Using 'Main Company' as default entity.")

            self.raw_subsidiaries = [{
                'id': 'main-company',
                'name': 'Main Company',
                'primary_domain': 'N/A'
            }]
            self.no_subsidiaries = True
            return
        meta = response['body']['meta']
        pagination = meta.get('pagination')
        offset = pagination.get('offset', 0)
        total = pagination.get('total', 0)
        single_response = response['body']['resources']
        if pagination:
            limit = 100
            while offset < total:
                cur_response = self.falcon.query_combined_ecosystem_subsidiaries(offset=offset, limit=limit)
                resource = cur_response['body']['resources']
                if resource:
                    self.raw_subsidiaries.extend(resource)
                offset += limit
        else:
            self.raw_subsidiaries.extend(single_response)

        if self.subsidiary_filter:
            filtered = [s for s in self.raw_subsidiaries if self.subsidiary_filter.lower() in s.get('name', '').lower()]
            if not filtered:
                raise SystemExit(f"No subsidiaries found matching filter: {self.subsidiary_filter}")
            self.raw_subsidiaries = filtered
            print(f"  Filtered to {len(filtered)} subsidiary(ies) matching '{self.subsidiary_filter}'")
        else:
            print(f"  Found {len(self.raw_subsidiaries)} subsidiary(ies)")

    def query_exposed_assets(self):
        print("\n[4/4] Querying exposed assets (Critical & High)...")
        for subsidiary in self.raw_subsidiaries:
            name = subsidiary.get('name', None)
            if self.no_subsidiaries:
                filter_str = "(criticality:'Critical',criticality:'High')"
            else:
                filter_str = f"(criticality:'Critical',criticality:'High')+subsidiaries.name:'{name}'"
            response = self.falcon.query_assets(filter=filter_str)

            code = response['status_code']
            if code != 200:
                raise SystemExit(f"Error querying exposed assets. Status code: {code}\n"
                               f"Details: {response.get('body', {}).get('errors', 'Unknown error')}")

            meta = response['body']['meta']
            pagination = meta.get('pagination')
            after = pagination.get('after')
            total = pagination.get('total')
            single_response = response['body']['resources']

            if after:
                all_ids = []
                limit = 100
                all_ids.extend(single_response)
                seen_ids = set(single_response)
                while after is not None:
                    cur_response = self.falcon.query_assets(filter=filter_str, limit=limit, after=after)
                    cur_ids = cur_response['body']['resources']
                    if not cur_ids:
                        break

                    new_ids = [cid for cid in cur_ids if cid not in seen_ids]
                    if not new_ids:
                        break

                    all_ids.extend(new_ids)
                    seen_ids.update(new_ids)

                    meta = cur_response['body']['meta']
                    pagination = meta.get('pagination', {})
                    after = pagination.get('after', None)

                exposed_assets = self._get_exposed_assets(all_ids)
                self.raw_assets[name] = exposed_assets
                print(f"  {name}: {len(all_ids)} asset(s)")
            else:
                exposed_assets = self._get_exposed_assets(single_response)
                self.raw_assets[name] = exposed_assets
                print(f"  {name}: {len(single_response)} asset(s)")


    def query_aggregate_data(self):
        print("\n[2/4] Aggregating asset data by criticality...")
        for subsidiary in self.raw_subsidiaries:
            name = subsidiary.get('name', None)
            if self.no_subsidiaries:
                filter_str = None
            else:
                filter_str = f"subsidiaries.name:'{name}'"
            response = self.falcon.aggregate_assets(field="criticality",
                                                    name=name,
                                                    type="terms",
                                                    filter=filter_str
                                                    )
            if response['status_code'] != 200:
                raise SystemExit(f"Error aggregating assets. Status code: {response['status_code']}\n"
                               f"Details: {response.get('body', {}).get('errors', 'Unknown error')}")
            resource = response['body']['resources'][0]
            self.raw_asset_summary.append(resource)
        print(f"  Aggregated data for {len(self.raw_asset_summary)} subsidiary(ies)")

    def query_applications(self):
        print("\n[3/4] Aggregating exposed applications...")
        for subsidiary in self.raw_subsidiaries:
            name = subsidiary.get('name', None)
            if self.no_subsidiaries:
                filter_str = None
            else:
                filter_str = f"subsidiaries.name:'{name}'"
            response = self.falcon.aggregate_assets(field="applications.name",
                                                    name=name,
                                                    type="terms",
                                                    filter=filter_str
                                                    )
            if response['status_code'] != 200:
                raise SystemExit(f"Error aggregating applications. Status code: {response['status_code']}\n"
                               f"Details: {response.get('body', {}).get('errors', 'Unknown error')}")
            resource = response['body']['resources'][0]
            self.raw_applications.append(resource)
        print(f"  Aggregated applications for {len(self.raw_applications)} subsidiary(ies)")

    def _get_exposed_assets(self, ids: list):
        all_assets = []
        if len(ids) > 100:
            chunks = [ids[x:x+100] for x in range(0, len(ids), 100)] # split ids into groupings of 100s
            for batch in chunks:
                data = self.falcon.get_assets(ids=batch)
                cur_ids = data['body']['resources']
                all_assets.extend(cur_ids)
            return all_assets

        data = self.falcon.get_assets(ids=ids)
        cur_ids = data['body']['resources']
        all_assets.extend(cur_ids)
        return all_assets

def connect_api(key: str, secret: str, debug: bool) -> ExposureManagement:
    """Connect to the CrowdStrike API and return an ExposureManagement instance.

    Parameters:
        key -- CrowdStrike API client ID. String.
        secret -- CrowdStrike API client secret. String.
        debug -- Enable debug logging. Boolean.

    Returns: ExposureManagement service class instance.
    """
    try:
        if debug:
            logging.basicConfig(level=logging.DEBUG)
        return ExposureManagement(client_id=key, client_secret=secret, debug=debug)
    except APIError as e:
        raise SystemExit(f"Failed to connect to API: {e}") from e

def build_subsidiaries(subsidiaries: list) -> list[Subsidiary]:
    all_subsidiaries = []
    for cur_sub in subsidiaries:
        cur_id = cur_sub.get('id', None)
        cur_name = cur_sub.get('name', None)
        cur_domain = cur_sub.get('primary_domain', None)
        
        sub_builder = Subsidiary(id=cur_id, name=cur_name, primary_domain=cur_domain)
        all_subsidiaries.append(sub_builder)

    return all_subsidiaries

def build_asset_summary(raw_asset_summary: list):
    all_asset_summaries = {}
    for index, value in enumerate(raw_asset_summary):
        name = value.get('name')
        buckets = value.get('buckets')
        total = 0
        new_asset_sum = AssetSummary()

        for bucket in buckets:
            label = bucket.get('label', None)
            count = bucket.get('count', None)
            if label is not None:
                if label == "Critical":
                    new_asset_sum.critical = count
                    total += count
                elif label == "Noncritical":
                    new_asset_sum.noncritical = count
                    total += count
                elif label == "High":
                    new_asset_sum.high = count
                    total += count
                elif label == "Unassigned":
                    new_asset_sum.unassigned = count
                    total += count
        new_asset_sum.total_assets = total

        all_asset_summaries[name] = new_asset_sum

    return all_asset_summaries

def build_applications(raw_applications: list):
    all_applications = {}
    for index, value in enumerate(raw_applications):
        name = value.get('name')
        buckets = value.get('buckets')
        apps = []
        for bucket in buckets:
            label = bucket.get('label', None)
            count = bucket.get('count', None)
            new_app = Application(name=label, count=count)
            apps.append(new_app)
        all_applications[name] = apps

    return all_applications

def build_important_assets(raw_assets: dict):
    all_assets = {}

    for key, assets in raw_assets.items():
        if not assets:
            continue
        important_assets = []
        for asset in assets:
            criticality = asset.get('criticality', None)
            asset_type = asset.get('asset_type', None)
            ip_dict = asset.get('ip', None)
            ip_address = ip_dict.get('ip_address') if ip_dict else None

            fqdn = None
            if ip_dict:
                fqdns = ip_dict.get('fqdns')
                if fqdns:
                    fqdn = fqdns[0] if isinstance(fqdns, list) and len(fqdns) > 0 else fqdns

            if not fqdn:
                dns_domain = asset.get('dns_domain', None)
                if dns_domain:
                    domain_fqdn = dns_domain.get('fqdn')
                    fqdn = domain_fqdn[0] if isinstance(domain_fqdn, list) and len(domain_fqdn) > 0 else domain_fqdn

            location = ip_dict.get('location') if ip_dict else None
            confidence = asset.get('confidence', None)
            status = asset.get('status', None)

            internet_exposure = asset.get('internet_exposure', None)
            perimeter = asset.get('perimeter', None)
            isp = ip_dict.get('isp') if ip_dict else None
            asn = ip_dict.get('asn') if ip_dict else None
            country_name = location.get('country_name') if location else None
            discovered_by = asset.get('discovered_by', None)

            triage = asset.get('triage', {})
            triage_status = triage.get('status') if triage else None
            triage_action = triage.get('action') if triage else None

            cur_imp_asset = ImportantAsset(criticality=criticality,
                                           asset_type=asset_type,
                                           ip_address=ip_address,
                                           fqdn=fqdn,
                                           confidence=confidence,
                                           status=status,
                                           location=location,
                                           internet_exposure=internet_exposure,
                                           perimeter=perimeter,
                                           isp=isp,
                                           asn=asn,
                                           country_name=country_name,
                                           triage_status=triage_status,
                                           triage_action=triage_action,
                                           discovered_by=discovered_by
                                           )
            important_assets.append(cur_imp_asset)

        important_assets.sort(key=attrgetter('criticality'))
        all_assets[key] = important_assets

    return all_assets

def build_enhanced_stats(raw_assets: dict):
    """Build enhanced statistics from raw asset data."""
    all_stats = {}

    for key, assets in raw_assets.items():
        if not assets:
            continue

        stats = EnhancedStats()
        stats.total_assets = len(assets)

        for asset in assets:
            if asset.get('internet_exposure') == 'Yes':
                stats.internet_exposed += 1

            perimeter = asset.get('perimeter')
            if perimeter and perimeter.lower() != 'official':
                stats.shadow_it += 1

            triage = asset.get('triage')
            if triage and triage.get('status'):
                stats.triaged += 1

            status = asset.get('status')
            if status:
                if status.lower() == 'online':
                    stats.online += 1
                elif status.lower() == 'offline':
                    stats.offline += 1

            discovered_by = asset.get('discovered_by')
            if discovered_by:
                if discovered_by.lower() == 'auto':
                    stats.auto_discovered += 1
                else:
                    stats.manual_discovered += 1

            ip_dict = asset.get('ip', {})
            location = ip_dict.get('location', {})
            country_name = location.get('country_name')
            if country_name:
                stats.countries[country_name] = stats.countries.get(country_name, 0) + 1

            isp = ip_dict.get('isp')
            if isp:
                stats.isps[isp] = stats.isps.get(isp, 0) + 1

        all_stats[key] = stats

    return all_stats

def build_discovery_paths(raw_assets: dict, limit=10):
    """Extract interesting discovery paths from assets."""
    all_paths = {}

    for key, assets in raw_assets.items():
        if not assets:
            continue

        paths = []
        count = 0

        for asset in assets:
            if count >= limit:
                break

            discovery = asset.get('discovery', {})
            path_data = discovery.get('path', {})
            steps = path_data.get('steps', [])

            if steps and len(steps) > 1:
                fqdn = None
                ip_dict = asset.get('ip', {})
                fqdns = ip_dict.get('fqdns')
                if fqdns:
                    fqdn = fqdns[0] if isinstance(fqdns, list) and len(fqdns) > 0 else fqdns

                if not fqdn:
                    dns_domain = asset.get('dns_domain', {})
                    domain_fqdn = dns_domain.get('fqdn')
                    fqdn = domain_fqdn[0] if isinstance(domain_fqdn, list) and len(domain_fqdn) > 0 else domain_fqdn

                if not fqdn:
                    fqdn = ip_dict.get('ip_address', 'Unknown')

                path = DiscoveryPath(
                    asset_id=asset.get('id'),
                    asset_fqdn=fqdn,
                    path_steps=steps,
                    criticality=asset.get('criticality')
                )
                paths.append(path)
                count += 1

        all_paths[key] = paths

    return all_paths

def aggregate_data(subsidiaries: list[Subsidiary],
                   asset_summaries: dict,
                   applications: dict,
                   assets: dict,
                   enhanced_stats: dict,
                   discovery_paths: dict
                   ) -> list[AggregateResults]:
    """Combine all the data together to create a report."""
    results = []

    for subsidiary in subsidiaries:
        name = subsidiary.name

        asset_summary = asset_summaries.get(name)
        app_list = applications.get(name, [])
        important_assets = assets.get(name, [])
        stats = enhanced_stats.get(name, EnhancedStats())
        paths = discovery_paths.get(name, [])

        agg_result = AggregateResults(
            name=name,
            subsidiary=subsidiary,
            asset_summary=asset_summary,
            applications=app_list,
            important_assets=important_assets,
            enhanced_stats=stats,
            discovery_paths=paths
        )

        results.append(agg_result)

    return results

def export_to_json(filename: str, aggregated_results: list[AggregateResults]) -> None:
    """Export aggregated results to JSON format.

    Parameters:
        filename -- Output filename.
        aggregated_results -- List of aggregated results.
    """
    export_data = {
        'export_timestamp': datetime.now().isoformat(),
        'subsidiaries': []
    }

    for result in aggregated_results:
        subsidiary_data = {
            'name': result.name,
            'subsidiary': asdict(result.subsidiary),
            'asset_summary': asdict(result.asset_summary) if result.asset_summary else None,
            'applications': [asdict(app) for app in result.applications],
            'important_assets': [asdict(asset) for asset in result.important_assets]
        }
        export_data['subsidiaries'].append(subsidiary_data)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Exported data to {filename}")

def export_to_csv(filename: str, aggregated_results: list[AggregateResults]) -> None:
    """Export aggregated results to CSV format.

    Parameters:
        filename -- Output filename.
        aggregated_results -- List of aggregated results.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'subsidiary_name', 'subsidiary_id', 'subsidiary_domain',
            'total_assets', 'critical_assets', 'high_assets', 'noncritical_assets', 'unassigned_assets',
            'asset_fqdn', 'asset_ip', 'asset_type', 'asset_criticality', 'asset_confidence', 'asset_status'
        ]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for result in aggregated_results:
            base_row = {
                'subsidiary_name': result.subsidiary.name,
                'subsidiary_id': result.subsidiary.id,
                'subsidiary_domain': result.subsidiary.primary_domain,
                'total_assets': result.asset_summary.total_assets if result.asset_summary else 0,
                'critical_assets': result.asset_summary.critical if result.asset_summary else 0,
                'high_assets': result.asset_summary.high if result.asset_summary else 0,
                'noncritical_assets': result.asset_summary.noncritical if result.asset_summary else 0,
                'unassigned_assets': result.asset_summary.unassigned if result.asset_summary else 0,
            }

            if result.important_assets:
                for asset in result.important_assets:
                    row = base_row.copy()
                    row['asset_fqdn'] = asset.fqdn or 'N/A'
                    row['asset_ip'] = asset.ip_address or 'N/A'
                    row['asset_type'] = asset.asset_type or 'N/A'
                    row['asset_criticality'] = asset.criticality or 'N/A'
                    row['asset_confidence'] = asset.confidence if asset.confidence else 'N/A'
                    row['asset_status'] = asset.status or 'N/A'
                    writer.writerow(row)
            else:
                writer.writerow(base_row)

    print(f"\n✓ Exported data to {filename}")

def main():
    args = parse_command_line()
    falcon = connect_api(key=args.client_id, secret=args.client_secret, debug=args.debug)
    interface = ExposedAssetsManager(falcon=falcon, subsidiary_filter=args.subsidiary)
    interface.query_subsidiaries()
    subsidiaries = build_subsidiaries(interface.raw_subsidiaries)

    interface.query_aggregate_data()
    asset_summaries = build_asset_summary(interface.raw_asset_summary)

    interface.query_applications()
    applications = build_applications(interface.raw_applications)

    interface.query_exposed_assets()
    assets = build_important_assets(interface.raw_assets)

    enhanced_stats = build_enhanced_stats(interface.raw_assets)
    discovery_paths = build_discovery_paths(interface.raw_assets, limit=10)

    aggregated_results = aggregate_data(subsidiaries,
                                        asset_summaries,
                                        applications,
                                        assets,
                                        enhanced_stats,
                                        discovery_paths
                                        )

    total_assets = sum(r.asset_summary.total_assets for r in aggregated_results if r.asset_summary and r.asset_summary.total_assets)
    critical_assets = sum(r.asset_summary.critical for r in aggregated_results if r.asset_summary and r.asset_summary.critical)
    high_assets = sum(r.asset_summary.high for r in aggregated_results if r.asset_summary and r.asset_summary.high)

    print("\n" + "="*60)
    print("Summary:")
    print(f"  Subsidiaries: {len(aggregated_results)}")
    print(f"  Total Assets: {total_assets}")
    print(f"  Critical: {critical_assets}")
    print(f"  High: {high_assets}")
    print("="*60)

    if args.format == 'json':
        export_to_json(args.output, aggregated_results)
    elif args.format == 'csv':
        export_to_csv(args.output, aggregated_results)
    else:
        print(f"\nGenerating PDF report: {args.output}")
        executive_report = ExposureManagementReport(file_name=args.output,
                                                    aggregated_results=aggregated_results,
                                                    dark_mode=args.dark,
                                                    logo_path=args.logo
                                                    )
        executive_report.build()

if __name__ == "__main__":
    main()
