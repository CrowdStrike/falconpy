"""
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
from .deprecated import _custom_ioa_deprecated
from .deprecated import _firewall_management_deprecated
from .deprecated import _installation_tokens_deprecated
from .deprecated import _iocs_deprecated
from .deprecated import _real_time_response_deprecated
from .deprecated import _real_time_response_admin_deprecated

from ._cloud_connect_aws import _cloud_connect_aws_endpoints
from ._cspm_registration import _cspm_registration_endpoints
from ._custom_ioa import _custom_ioa_endpoints
from ._d4c_registration import _d4c_registration_endpoints
from ._detects import _detects_endpoints
from ._device_control_policies import _device_control_policies_endpoints
from ._event_streams import _event_streams_endpoints
from ._falcon_complete_dashboard import _falcon_complete_dashboard_endpoints
from ._falconx_sandbox import _falconx_sandbox_endpoints
from ._firewall_management import _firewall_management_endpoints
from ._firewall_policies import _firewall_policies_endpoints
from ._host_group import _host_group_endpoints
from ._hosts import _hosts_endpoints
from ._incidents import _incidents_endpoints
from ._installation_tokens import _installation_tokens_endpoints
from ._intel import _intel_endpoints
from ._ioa_exclusions import _ioa_exclusions_endpoints
from ._iocs import _iocs_endpoints
from ._malquery import _malquery_endpoints
from ._ml_exclusions import _ml_exclusions_endpoints
from ._mssp import _mssp_endpoints
from ._oauth2 import _oauth2_endpoints
from ._overwatch_dashboard import _overwatch_dashboard_endpoints
from ._prevention_policies import _prevention_policies_endpoints
from ._quick_scan import _quick_scan_endpoints
from ._real_time_response import _real_time_response_endpoints
from ._real_time_response_admin import _real_time_response_admin_endpoints
from ._sample_uploads import _sample_uploads_endpoints
from ._sensor_download import _sensor_download_endpoints
from ._sensor_update_policies import _sensor_update_policies_endpoints
from ._sensor_visibility_exclusions import _sensor_visibility_exclusions_endpoints
from ._spotlight_vulnerabilities import _spotlight_vulnerabilities_endpoints
from ._user_management import _user_management_endpoints
from ._zero_trust_assessment import _zero_trust_assessment_endpoints

api_endpoints = []
api_endpoints.extend(_cloud_connect_aws_endpoints)
api_endpoints.extend(_cspm_registration_endpoints)
api_endpoints.extend(_custom_ioa_endpoints)
api_endpoints.extend(_d4c_registration_endpoints)
api_endpoints.extend(_detects_endpoints)
api_endpoints.extend(_device_control_policies_endpoints)
api_endpoints.extend(_event_streams_endpoints)
api_endpoints.extend(_falcon_complete_dashboard_endpoints)
api_endpoints.extend(_falconx_sandbox_endpoints)
api_endpoints.extend(_firewall_management_endpoints)
api_endpoints.extend(_firewall_policies_endpoints)
api_endpoints.extend(_host_group_endpoints)
api_endpoints.extend(_hosts_endpoints)
api_endpoints.extend(_incidents_endpoints)
api_endpoints.extend(_installation_tokens_endpoints)
api_endpoints.extend(_intel_endpoints)
api_endpoints.extend(_ioa_exclusions_endpoints)
api_endpoints.extend(_iocs_endpoints)
api_endpoints.extend(_malquery_endpoints)
api_endpoints.extend(_ml_exclusions_endpoints)
api_endpoints.extend(_mssp_endpoints)
api_endpoints.extend(_oauth2_endpoints)
api_endpoints.extend(_overwatch_dashboard_endpoints)
api_endpoints.extend(_prevention_policies_endpoints)
api_endpoints.extend(_quick_scan_endpoints)
api_endpoints.extend(_real_time_response_endpoints)
api_endpoints.extend(_real_time_response_admin_endpoints)
api_endpoints.extend(_sample_uploads_endpoints)
api_endpoints.extend(_sensor_download_endpoints)
api_endpoints.extend(_sensor_update_policies_endpoints)
api_endpoints.extend(_sensor_visibility_exclusions_endpoints)
api_endpoints.extend(_spotlight_vulnerabilities_endpoints)
api_endpoints.extend(_user_management_endpoints)
api_endpoints.extend(_zero_trust_assessment_endpoints)

# Deprecated endpoints
deprecated_endpoints = []
deprecated_endpoints.extend(_custom_ioa_deprecated)
deprecated_endpoints.extend(_firewall_management_deprecated)
deprecated_endpoints.extend(_installation_tokens_deprecated)
deprecated_endpoints.extend(_iocs_deprecated)
deprecated_endpoints.extend(_real_time_response_deprecated)
deprecated_endpoints.extend(_real_time_response_admin_deprecated)

# api_endpoints contains all endpoints, production and deprecated
api_endpoints.extend(deprecated_endpoints)
