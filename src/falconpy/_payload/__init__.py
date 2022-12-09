"""The CrowdStrike Falcon OAuth2 API SDK payloads module.

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
from ._generic import (
    generic_payload_list,
    aggregate_payload,
    exclusion_payload,
    installation_token_payload,
    simple_action_parameter,
    token_settings_payload
    )
from ._host_group import host_group_create_payload, host_group_update_payload
from ._recon import (
    recon_action_payload,
    recon_action_update_payload,
    recon_rules_payload,
    recon_notifications_payload,
    recon_rule_preview_payload,
    recon_export_job_payload
    )
from ._malquery import malquery_exact_search_payload, malquery_hunt_payload, malquery_fuzzy_payload
from ._container import image_payload
from ._detects import update_detects_payload
from ._incidents import incident_action_parameters
from ._ioa import ioa_exclusion_payload, ioa_custom_payload
from ._prevention_policy import prevention_policy_payload
from ._sensor_update_policy import sensor_policy_payload
from ._response_policy import response_policy_payload
from ._real_time_response import command_payload, data_payload
from ._cloud_connect_aws import aws_registration_payload
from ._ioc import indicator_payload, indicator_update_payload, indicator_report_payload
from ._d4c_registration import azure_registration_payload, aws_d4c_registration_payload
from ._cspm_registration import cspm_registration_payload, cspm_policy_payload, cspm_scan_payload
from ._device_control_policy import device_policy_payload
from ._falconx import falconx_payload
from ._mssp import mssp_payload
from ._firewall import (
    firewall_policy_payload,
    firewall_container_payload,
    firewall_rule_group_validation_payload,
    firewall_rule_group_payload,
    firewall_rule_group_update_payload,
    firewall_filepattern_payload,
    network_locations_metadata_payload,
    network_locations_create_payload
    )
from ._reports import reports_payload
from ._message_center import activity_payload, case_payload
from ._alerts import update_alerts_payload
from ._sample_uploads import extraction_payload
from ._ods import scheduled_scan_payload, scans_report_payload


__all__ = [
    "generic_payload_list", "aggregate_payload", "recon_action_payload", "recon_rules_payload",
    "recon_action_update_payload", "recon_notifications_payload", "recon_rule_preview_payload",
    "malquery_exact_search_payload", "malquery_hunt_payload", "malquery_fuzzy_payload",
    "update_detects_payload", "exclusion_payload", "ioa_exclusion_payload",
    "host_group_create_payload", "host_group_update_payload", "installation_token_payload",
    "prevention_policy_payload", "sensor_policy_payload", "response_policy_payload",
    "command_payload", "data_payload", "aws_registration_payload", "indicator_payload",
    "indicator_update_payload", "azure_registration_payload", "cspm_registration_payload",
    "cspm_policy_payload", "cspm_scan_payload", "device_policy_payload", "falconx_payload",
    "mssp_payload", "ioa_custom_payload", "firewall_policy_payload", "firewall_container_payload",
    "firewall_rule_group_payload", "firewall_rule_group_update_payload", "reports_payload",
    "activity_payload", "case_payload", "incident_action_parameters", "update_alerts_payload",
    "firewall_rule_group_validation_payload", "firewall_filepattern_payload",
    "aws_d4c_registration_payload", "image_payload", "indicator_report_payload",
    "extraction_payload", "simple_action_parameter", "network_locations_metadata_payload",
    "network_locations_create_payload", "scheduled_scan_payload", "scans_report_payload",
    "token_settings_payload", "recon_export_job_payload"
]
