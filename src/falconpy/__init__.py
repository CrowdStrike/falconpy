"""The CrowdStrike Falcon OAuth2 API SDK

 @@@@@@@  @@@@@@@    @@@@@@   @@@  @@@  @@@  @@@@@@@    @@@@@@   @@@@@@@  @@@@@@@   @@@  @@@  @@@  @@@@@@@@
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@  @@@  @@@  @@@@@@@@
!@@       @@!  @@@  @@!  @@@  @@!  @@!  @@!  @@!  @@@  !@@         @@!    @@!  @@@  @@!  @@!  !@@  @@!
!@!       !@!  @!@  !@!  @!@  !@!  !@!  !@!  !@!  @!@  !@!         !@!    !@!  @!@  !@!  !@!  @!!  !@!
!@!       @!@!!@!   @!@  !@!  @!!  !!@  @!@  @!@  !@!  !!@@!!      @!!    @!@!!@!   !!@  @!@@!@!   @!!!:!
!!!       !!@!@!    !@!  !!!  !@!  !!!  !@!  !@!  !!!   !!@!!!     !!!    !!@!@!    !!!  !!@!!!    !!!!!:
:!!       !!: :!!   !!:  !!!  !!:  !!:  !!:  !!:  !!!       !:!    !!:    !!: :!!   !!:  !!: :!!   !!:
:!:       :!:  !:!  :!:  !:!  :!:  :!:  :!:  :!:  !:!      !:!     :!:    :!:  !:!  :!:  :!:  !:!  :!:
 ::: :::  ::   :::  ::::: ::   :::: :: :::    :::: ::  :::: ::      ::    ::   :::   ::   ::  :::   :: ::::
 :: :: :   :   : :   : :  :     :: :  : :    :: :  :   :: : :       :      :   : :  :     :   :::  : :: ::

                                                         _______       __                  _______
                                                        |   _   .---.-|  .----.-----.-----|   _   .--.--.
                                                        |.  1___|  _  |  |  __|  _  |     |.  1   |  |  |
                                                        |.  __) |___._|__|____|_____|__|__|.  ____|___  |
                                                        |:  |                             |:  |   |_____|
                                                        |::.|     CrowdStrike Falcon      |::.|
                                                        `---' OAuth2 API SDK for Python 3 `---'
"""
from ._version import _VERSION, _MAINTAINER, _AUTHOR, _AUTHOR_EMAIL
from ._version import _CREDITS, _DESCRIPTION, _TITLE, _PROJECT_URL
from ._version import _DOCS_URL, _KEYWORDS
from .api_complete import APIHarness
from .cloud_connect_aws import CloudConnectAWS
from .cspm_registration import CSPMRegistration
from .custom_ioa import CustomIOA
from .d4c_registration import D4CRegistration
from .detects import Detects
from .device_control_policies import DeviceControlPolicies
from .event_streams import EventStreams
from .falcon_complete_dashboard import CompleteDashboard
from .falcon_container import FalconContainer
from .falconx_sandbox import FalconXSandbox
from .firewall_management import FirewallManagement
from .firewall_policies import FirewallPolicies
from .host_group import HostGroup
from .hosts import Hosts
from .identity_protection import IdentityProtection
from .incidents import Incidents
from .installation_tokens import InstallationTokens
from .intel import Intel
from .ioa_exclusions import IOAExclusions
from .ioc import IOC
from .iocs import Iocs
from .kubernetes_protection import KubernetesProtection
from .malquery import MalQuery
from .ml_exclusions import MLExclusions
from .mssp import FlightControl
from .oauth2 import OAuth2
from .overwatch_dashboard import OverwatchDashboard
from .prevention_policy import PreventionPolicy
from .quarantine import Quarantine
from .quick_scan import QuickScan
from .real_time_response_admin import RealTimeResponseAdmin
from .real_time_response import RealTimeResponse
from .recon import Recon
from .report_executions import ReportExecutions
from .response_policies import ResponsePolicies
from .sample_uploads import SampleUploads
from .scheduled_reports import ScheduledReports
from .sensor_download import SensorDownload
from .sensor_update_policy import SensorUpdatePolicy
from .sensor_visibility_exclusions import SensorVisibilityExclusions
from .spotlight_vulnerabilities import SpotlightVulnerabilities
from .user_management import UserManagement
from .zero_trust_assessment import ZeroTrustAssessment

__version__ = _VERSION
__maintainer__ = _MAINTAINER
__author__ = _AUTHOR
__author_email__ = _AUTHOR_EMAIL
__credits__ = _CREDITS
__description__ = _DESCRIPTION
__title__ = _TITLE
__project_url__ = _PROJECT_URL
__docs_url__ = _DOCS_URL
__keywords__ = _KEYWORDS
__all__ = [
    "APIHarness", "CloudConnectAWS", "CSPMRegistration", "CustomIOA", "D4CRegistration",
    "Detects", "DeviceControlPolicies", "EventStreams", "CompleteDashboard",
    "FalconContainer", "FalconXSandbox", "FirewallManagement", "FirewallPolicies", "HostGroup",
    "Hosts", "IdentityProtection", "Incidents", "InstallationTokens", "Intel", "IOAExclusions",
    "IOC", "Iocs", "KubernetesProtection", "MalQuery", "MLExclusions", "FlightControl", "OAuth2",
    "OverwatchDashboard", "PreventionPolicy", "Quarantine", "QuickScan", "RealTimeResponseAdmin",
    "RealTimeResponse", "Recon", "ReportExecutions", "ResponsePolicies", "SampleUploads",
    "ScheduledReports", "SensorDownload", "SensorUpdatePolicy", "SensorVisibilityExclusions",
    "SpotlightVulnerabilities", "UserManagement", "ZeroTrustAssessment"
 ]
"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

⢻⣄
 ⠹⣿⣦         ⣦
  ⠈⣿⣿⣶⡀      ⠈⢿⣦
    ⠙⣿⣿⣿⣄      ⠹⣿⣶
      ⠙⣿⣿⣿⣶⣀     ⠻⣿⣿⣤
   ⠹⣄   ⠈⠻⣿⣿⣿⣶⡀    ⠙⢿⣿⣿⣤
    ⠙⣿⣦    ⠙⢿⣿⣿⣿⣶⣀   ⠈⠛⣿⣿⣿⣶⣄
      ⠛⣿⣷⣤    ⠙⢿⣿⣿⣿⣷⣤   ⠈⠛⣿⣿⣿⣿⣶⣤
        ⠙⣿⣿⣷⣤    ⠉⠻⣿⣿⣿⣿⣦⡀  ⠈⠻⣿⣿⣿⣿⣿⣿⣶⣤⣀
          ⠈⠛⣿⣿⣿⣶⡀   ⠈⠙⢿⣿⣿⣿⣶⡀  ⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣄⡀
             ⠈⠙⢿⣿⣿⣷⣤⡀   ⠉⠛⢿⣿⣿⣄  ⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄
                 ⠉⠛⢿⣿⣿⣿⣤⡀   ⠙⢿⣿⣦  ⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀
                     ⠉⠛⢿⣿⣿⣶⣄   ⠙⣿⡀ ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
                          ⠉⠻⣿⣷⣄  ⠙⡄  ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶
                              ⠙⢿⣦     ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                 ⠻⣆    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                  ⠈⠲⣀              ⠁     ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
                     ⠻⣷⣤⣀    ⠛⢶⣤⣀         ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                       ⠈⠛⣿⣿⣿⣶⣶⣶⣼⣿⣿⣷⣦⡀   ⣀   ⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄
                           ⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⡀ ⠈⢶⣤   ⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣀
                                  ⠉⠙⠛⠿⣿⣿⣿⣦  ⠻⣿⣷⣶⣤⣀⣀⣀ ⣀⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣮⣭⣉⠛⠿⣿⣿⣿⣿⣦⠙⣷
                                         ⠉⠛⠶⡀ ⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣍⠻⣿⣿⣿⣷⡀
                                                ⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠷⠌⠻⣿⣿⣦
                                               ⠉⣶⣀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉           ⠙⣿
                                                 ⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
     WE  STOP                                        ⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣤⣤⣤
     BREACHES                                          ⠈⠙⠛⠿⠛⠉⣿⣿⣿⠋     ⢿⡇
                                                             ⢻⣿⣄      ⠈⠈
                                                               ⠈⠉ FalconPy
"""
