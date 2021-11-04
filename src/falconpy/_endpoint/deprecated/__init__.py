"""The CrowdStrike Falcon OAuth2 API SDK deprecated endpoints module.

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
#                                                                             .---.        .-----------
#                                                                            /     \  __  /    ------
#                                                                           / /     \(..)/    -----
#  _____                                     __            __              //////   ' \/ `   ---
# |     \.-----.-----.----.-----.----.---.-.|  |_.-----.--|  |            //// / // :    : ---
# |  --  |  -__|  _  |   _|  -__|  __|  _  ||   _|  -__|  _  |           // /   /  /`    '--
# |_____/|_____|   __|__| |_____|____|___._||____|_____|_____|          //          //..\\
#              |__|                                                                UU    UU
# The following operations reference legacy naming convention and are considered deprecated.
# These operation IDs are maintained for backwards compatibility purposes only, Move all code
# references to use the new operations IDs defined above that align with the IDs defined in
# the service classes.
from ._custom_ioa import _custom_ioa_endpoints
from ._discover import _discover_endpoints
from ._firewall_management import _firewall_management_endpoints
from ._identity_protection import _identity_protection_endpoints
from ._installation_tokens import _installation_tokens_endpoints
from ._ioc import _ioc_endpoints
from ._iocs import _iocs_endpoints
from ._real_time_response import _real_time_response_endpoints
from ._real_time_response_admin import _real_time_response_admin_endpoints
from ._report_executions import _report_executions_endpoints
from ._scheduled_reports import _scheduled_reports_endpoints

_custom_ioa_deprecated = _custom_ioa_endpoints
_discover_deprecated = _discover_endpoints
_firewall_management_deprecated = _firewall_management_endpoints
_identity_protection_deprecated = _identity_protection_endpoints
_installation_tokens_deprecated = _installation_tokens_endpoints
_ioc_deprecated = _ioc_endpoints
_iocs_deprecated = _iocs_endpoints
_real_time_response_deprecated = _real_time_response_endpoints
_real_time_response_admin_deprecated = _real_time_response_admin_endpoints
_report_executions_deprecated = _report_executions_endpoints
_scheduled_reports_deprecated = _scheduled_reports_endpoints
