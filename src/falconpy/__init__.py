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
from ._version import _VERSION, _MAINTAINER, _AUTHOR, _AUTHOR_EMAIL
from ._version import _CREDITS, _DESCRIPTION, _TITLE, _PROJECT_URL
from ._version import _DOCS_URL, _KEYWORDS

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

⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀
⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠹⣿⣶
⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣶⣀⠀⠀⠀⠀⠀⠻⣿⣿⣤
⠀⠀⠀⠹⣄⠀⠀⠀⠈⠻⣿⣿⣿⣶⡀⠀⠀⠀⠀⠙⢿⣿⣿⣤
⠀⠀⠀⠀⠙⣿⣦⠀⠀⠀⠀⠙⢿⣿⣿⣿⣶⣀⠀⠀⠀⠈⠛⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠛⣿⣷⣤⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⣤⠀⠀⠀⠈⠛⣿⣿⣿⣿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣷⣤⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣦⡀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣶⣤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣶⡀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣶⡀⠀⠀⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣷⣤⡀⠀⠀⠀⠉⠛⢿⣿⣿⣄⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣤⡀⠀⠀⠀⠙⢿⣿⣦⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣶⣄⠀⠀⠀⠙⣿⡀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⣄⠀⠀⠙⡄⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣤⣀⠀⠀⠀⠀⠛⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣶⣶⣶⣼⣿⣿⣷⣦⡀⠀⠀⠀⣀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠈⢶⣤⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣿⣿⣿⣦⠀⠀⠻⣿⣷⣶⣤⣀⣀⣀⠀⣀⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣮⣭⣉⠛⠿⣿⣿⣿⣿⣦⠙⣷⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⡀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣍⠻⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠷⠌⠻⣿⣿⣦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣶⣀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀WE  STOP      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣤⣤⣤⠀
⠀⠀⠀⠀⠀BREACHES⠀⠀⠀⠀⠀⠀  ⠀         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠛⠉⣿⣿⣿⠋⠀⠀⠀⠀⠀⢿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢻⣿⣄⠀ ⠀⠀⠈⠈⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠈⠉⠀FalconPy
"""
