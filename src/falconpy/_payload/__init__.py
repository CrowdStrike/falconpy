"""The CrowdStrike Falcon OAuth2 API SDK payloads module

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
from ._generic import generic_payload_list, aggregate_payload, exclusion_payload
from ._generic import installation_token_payload
from ._host_group import host_group_create_payload, host_group_update_payload
from ._recon import recon_action_payload, recon_action_update_payload, recon_rules_payload
from ._recon import recon_notifications_payload, recon_rule_preview_payload
from ._malquery import malquery_exact_search_payload, malquery_hunt_payload, malquery_fuzzy_payload
from ._detects import update_detects_payload
from ._ioa import ioa_exclusion_payload
from ._prevention_policy import prevention_policy_payload
from ._sensor_update_policy import sensor_policy_payload

__all__ = [
    "generic_payload_list", "aggregate_payload", "recon_action_payload", "recon_rules_payload",
    "recon_action_update_payload", "recon_notifications_payload", "recon_rule_preview_payload",
    "malquery_exact_search_payload", "malquery_hunt_payload", "malquery_fuzzy_payload",
    "update_detects_payload", "exclusion_payload", "ioa_exclusion_payload",
    "host_group_create_payload", "host_group_update_payload", "installation_token_payload",
    "prevention_policy_payload", "sensor_policy_payload"
]
