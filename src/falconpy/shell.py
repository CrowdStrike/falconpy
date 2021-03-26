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
    shell.py - FalconShell                              |.  1___|  _  |  |  __|  _  |     |.  1   |  |  |
                                                        |.  __) |___._|__|____|_____|__|__|.  ____|___  |
    This is what happens when                           |:  |                             |:  |   |_____|
    the debugger grows up!                              |::.|     CrowdStrike Falcon      |::.|
                                                        `---' OAuth2 API SDK for Python 3 `---'

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
"""
import json
import sys
import os
import importlib
import logging
try:
    from . import api_complete as FalconSDK
    from ._shell._constant import _version
    from ._shell._shell import FalconShell

except ModuleNotFoundError:
    msg = "{}Unable to locate FalconPy library.{}\n".format("\033[91m", "\033[93m")
    msg = msg + "You must have FalconPy in your path or have the pip package installed in order to run FalconShell.{}".format(
        "\033[0m"
    )
    print(msg)
    sys.exit(1)

except ImportError:
    msg = "{}Unable to load FalconPy library.{}\n".format("\033[91m", "\033[93m")
    msg = msg + "This module is not intended to be run outside of the FalconPy package.\n"
    msg = msg + "Try python3 -m falconpy.shell instead.{}".format(
        "\033[0m"
    )
    print(msg)
    sys.exit(1)

# Logging setup
logging.basicConfig(filename='falcon-shell.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )
logger = logging.getLogger('FalconShell')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '\033[1m%(asctime)s\033[0m - \033[91m%(name)s\033[0m - \033[93m%(levelname)s\033[0m \n%(message)s'
    )
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
debug_started = False


class Console(FalconShell):

    def complete_command(self, text, line, begidx, endidx):
        return [i for i in self.complete_list if i.startswith(text) and "-" not in i]

    def _load(self: object, config_file: str = "config.json", item: str = "config"):
        try:
            # elm = eval("self."+item)
            with open(config_file, 'r') as _:
                exec("self."+item+" = json.loads(_.read())")
                if item.lower() == "config":
                    elm = self.config
                    if "active_debug" in elm:
                        if str(elm["active_debug"]).lower() == "true":
                            self.active_debug = True
                            logger.addHandler(ch)
                        else:
                            self.active_debug = False
                            logger.removeHandler(ch)
                    else:
                        self.active_debug = False
                        logger.removeHandler(ch)
                    if "debug" in elm:
                        if str(elm["debug"]).lower() == "true":
                            self.debug = True
                        else:
                            self.debug = False
                    else:
                        self.debug = True
                print(f"File {config_file} loaded to {item} object {self.Colors.OKGREEN}successfully{self.Colors.ENDC}.")
        except FileNotFoundError:
            print(f"Configuration file {self.Colors.FAIL}not found{self.Colors.ENDC}.")

    def _save(self: object, item: str, config_file: str):
        try:
            if (eval("self."+item)):
                fh = open(config_file, "w")
                json.dump(eval("self."+item), fh, indent=4)
                print(f"{item} object exported to {config_file} {self.Colors.OKGREEN}successfully{self.Colors.ENDC}.")
            else:
                print("{}Error 715{}: {}That object is currently empty{}.".format(self.Colors.FAIL,
                                                                                  self.Colors.ENDC,
                                                                                  self.Colors.WARNING,
                                                                                  self.Colors.ENDC
                                                                                  ))
        except AttributeError:
            print("{}Error 714{}: {}That object does not currently exist{}.".format(self.Colors.FAIL,
                                                                                    self.Colors.ENDC,
                                                                                    self.Colors.WARNING,
                                                                                    self.Colors.ENDC
                                                                                    ))

    def _connect(self: object):
        if self.config:
            self.falcon = FalconSDK.APIHarness(creds={
                    'client_id': self.config["falcon_client_id"],
                    'client_secret': self.config["falcon_client_secret"]
                }
            )
            # Enable auto-complete
            self.complete_list = [x[0] for x in self.falcon.commands]
            # for x in self.falcon.commands:
            #     self.completenames(x[0])
            # self.completenames = self.completenames.append(complete_list)
            if self.falcon.authenticate():
                self.cid = self.falcon.command("GetDeviceDetails",
                                               ids=self.falcon.command("QueryDevicesByFilter")["body"]["resources"][0]
                                               )["body"]["resources"][0]["cid"]
                print("{}Successfully{} authenticated to {}{}{}.".format(self.Colors.OKGREEN,
                                                                         self.Colors.ENDC,
                                                                         self.Colors.OKBLUE,
                                                                         self.cid,
                                                                         self.Colors.ENDC
                                                                         ))
            else:
                print(f"{self.Colors.FAIL}Unable to authenticate{self.Colors.ENDC} using the provided credentials.")

    def _api_action(self: object, command: dict):
        msg = ""
        if "return" not in command:
            command["return"] = None
        try:
            if command["action"].lower() == "show":
                msg = msg + json.dumps(command, indent=4)
            else:
                runner = command["action"]
                msg = msg + f"{self.Colors.OKBLUE}"
                msg = msg + "%s\n" % str("=" * (len("Executing "+runner) + 4))
                msg = msg + f"{self.Colors.ENDC} Results for{self.Colors.OKCYAN} {runner}\n{self.Colors.OKBLUE}"
                msg = msg + "%s\n" % str("=" * (len("Executing "+runner) + 4))
                msg = msg + f"{self.Colors.ENDC}"
                result = self.falcon.command(action=command["action"],
                                             parameters=command["params"],
                                             body=command["body"],
                                             action_name=command["action_name"],
                                             ids=command["ids"]
                                             )

                if self.debugging():
                    logger.debug(json.dumps(result, indent=4))
                if result["status_code"] in [200, 201]:
                    qt = result["body"]["meta"]["query_time"]
                    del result["body"]["meta"]
                    del result["body"]["errors"]
                    return_to = None
                    if command["return"]:
                        if ":" in command["return"]:
                            command["return"], return_to = command["return"].split(":", 1)
                        row = 0
                        do_row = False
                        try:
                            if int(command["return"]):
                                row = int(command["return"])
                                do_row = True
                            elif str(command["return"]) == "0":
                                row = 0
                                do_row = True
                        except ValueError:
                            pass
                        if do_row:
                            msg = msg + "Row "+command["return"]+": "
                            if type(result["body"]["resources"][row]) in [dict, list]:
                                msg = msg + json.dumps(result["body"]["resources"][row], indent=4)
                            else:
                                msg = msg + result["body"]["resources"][row]
                            if return_to:
                                self.do_set("{} {}".format(return_to.replace(":", " "), result["body"]["resources"][row]))
                        else:
                            if command["return"] in result["body"]["resources"][row]:  # TODO: Can't just take the first always
                                msg = command["return"]+": "+result["body"]["resources"][row][command["return"]]
                                if return_to:
                                    self.do_set("{} {}".format(
                                        return_to.replace(":", " "),
                                        result["body"]["resources"][row][command["return"]]
                                        ))
                    else:
                        try:
                            if "stdout" in result["body"]["resources"][0]:
                                msg = msg + result["body"]["resources"][0]["stdout"]
                            else:
                                msg = msg + json.dumps(result["body"], indent=4)
                        except IndexError:
                            msg = msg + json.dumps(result["body"], indent=4)
                    msg = msg + f"\n\nTotal execution time: {self.Colors.OKCYAN}{qt}{self.Colors.ENDC} seconds"
                    self.result.append(result)
                else:
                    msg = msg + "{}{}Error {}{}: {}{}{}".format(self.Colors.BOLD,
                                                                self.Colors.FAIL,
                                                                result["status_code"],
                                                                self.Colors.ENDC,
                                                                self.Colors.WARNING,
                                                                result["body"]["errors"][0]["message"],
                                                                self.Colors.ENDC
                                                                )
        except Exception as e:
            err = str(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            msg = f"{self.Colors.FAIL}Exception {exc_type.__name__} was generated "
            msg = msg + f"on line {exc_tb.tb_lineno} in {fname}{self.Colors.ENDC}: {err}"
            del(exc_type, exc_obj, exc_tb)
        # pydoc.pipepager(msg, cmd='less -F -X -R --quit-if-one-screen')
        print(msg)

    def _execute(self: object, args):
        try:
            go = {}
            go["return"] = None
            cmds = args.split(" ")
            cnt = 1
            for c in cmds:
                if "=" in c:
                    key, val = c.rsplit("=", 1)
                    if "{" in val:
                        go[key] = json.loads(val)
                    else:
                        go[key] = val
                else:
                    if cnt == 1:
                        go["action"] = c
                cnt += 1
            if self.returned:
                go["return"] = self.returned
            if self.falcon.authenticated:
                # TODO: Add additional api_complete.command parameters
                self._api_action({"action": go["action"],
                                  "params": self.params,
                                  "body": self.body,
                                  "action_name": self.action_name,
                                  "ids": self.ids,
                                  "return": go["return"]
                                  })
                # print("Result: {}".format(self.result))
            else:
                print(f"{self.Colors.FAIL}Not connected{self.Colors.ENDC}.")
        except Exception as e:
            err = str(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            msg = f"{self.Colors.FAIL}Exception {exc_type.__name__} was generated "
            msg = msg + f"on line {exc_tb.tb_lineno} in {fname}{self.Colors.ENDC}: {err}"
            del(exc_type, exc_obj, exc_tb)
            print(msg)

    def _quit(self: object, args):
        try:
            if self.falcon.authenticated:
                self.falcon.deauthenticate()
        except AttributeError:
            pass
        raise SystemExit()

    def _shell(self: object, args):
        os.system(args)

    def do_load(self: object, args):
        """Grab the file and load it to the object."""
        try:
            comm, lfile = args.split(" ", 2)
            self._load(item=comm, config_file=lfile)
        except (AttributeError, ValueError):
            print("{}Error 711{}: {}Invalid command syntax.{}\n".format(self.Colors.FAIL,
                                                                        self.Colors.ENDC,
                                                                        self.Colors.WARNING,
                                                                        self.Colors.ENDC
                                                                        ))
            print("Command format: {}load{} {}item{} filename".format(self.Colors.UNDERLINE,
                                                                      self.Colors.ENDC,
                                                                      self.Colors.BOLD,
                                                                      self.Colors.ENDC
                                                                      ))

    def do_save(self: object, args):
        """Save the object ot a file (JSON format)."""
        try:
            comm, lfile = args.split(" ", 2)
            self._save(item=comm, config_file=lfile)
        except (AttributeError, ValueError):
            print("{}Error 713{}: {}Invalid command syntax.{}\n".format(self.Colors.FAIL,
                                                                        self.Colors.ENDC,
                                                                        self.Colors.WARNING,
                                                                        self.Colors.ENDC
                                                                        ))
            print("Command format: {}save{} {}item{} filename".format(self.Colors.UNDERLINE,
                                                                      self.Colors.ENDC,
                                                                      self.Colors.BOLD,
                                                                      self.Colors.ENDC
                                                                      ))

    def do_connect(self: object, args):
        """Connect to the Falcon API using the credentials in your configuration file."""
        self._connect()

    def do_exit(self: object, args):
        """Quit FalconShell."""
        self._quit(args)

    def do_quit(self: object, args):
        """Quit FalconShell."""
        self._quit(args)

    def do_status(self: object, args):
        """Returns the current connection status."""
        try:
            if self.falcon.authenticated:
                msg = f"{self.Colors.OKGREEN}Connected to {self.Colors.OKBLUE}{self.cid}.{self.Colors.ENDC}"
            else:
                msg = f"{self.Colors.FAIL}Not connected{self.Colors.ENDC}."
        except AttributeError:
            msg = f"{self.Colors.FAIL}Not connected{self.Colors.ENDC}."

        print(msg)

    def do_clear(self: object, args):
        """Clears the current screen display, body and parameter payloads"""
        args = args.lower()
        if args == "body":
            self.body = {}
        elif args == "params":
            self.params = {}
        elif args == "action_name":
            self.action_name = None
        elif args == "ids":
            self.ids = None
        elif args == "commands":
            self.commands = []
        elif args == "result":
            self.result = []
        elif args == "returned":
            self.returned = None
        elif args:
            try:
                exec("del(self."+args+")")
            except AttributeError:
                pass
        else:
            self._header()

    def do_egg(self: object, args):
        """I recommend you just try it."""
        self._egg(args)

    def emptyline(self: object):
        pass

    def default(self: object, args):
        try:
            if self.active_debug:
                logger.addHandler(ch)
                msg = ""
                msg = msg + f"{self.Colors.WARNING}"
                msg = msg + "%s\n" % str("=" * (len("Active debugging enabled") + 2))
                msg = msg + "{} Active debugging{} enabled{}\n{}".format(self.Colors.ENDC,
                                                                         self.Colors.OKCYAN,
                                                                         self.Colors.ENDC,
                                                                         self.Colors.WARNING
                                                                         )
                msg = msg + "%s\n" % str("=" * (len("Active debugging enabled") + 2))
                msg = msg + f"{self.Colors.ENDC}"
                print(msg)
            else:
                logger.removeHandler(ch)

            self._execute(args)
        except AttributeError:
            print(f"{self.Colors.FAIL}Invalid command syntax{self.Colors.ENDC}.")

    def do_debug(self: object, args):
        """Enable / disable logfile debugging."""
        if "false" in args.lower():
            self.debug = False
            print(f"Debug log has been {self.Colors.FAIL}disabled{self.Colors.ENDC}.")
        if "true" in args.lower():
            self.debug = True
            print(f"Debug log has been {self.Colors.OKGREEN}enabled{self.Colors.ENDC}.")

    def do_active_debug(self: object, args):
        """Enable / disable console debugging."""
        if "false" in args.lower():
            self.active_debug = False
            logger.removeHandler(ch)
            print(f"Active debugging has been {self.Colors.FAIL}disabled{self.Colors.ENDC}.")
        if "true" in args.lower():
            self.active_debug = True
            logger.addHandler(ch)
            print(f"Active debugging has been {self.Colors.OKGREEN}enabled{self.Colors.ENDC}.")

    def do_show(self: object, args):
        """Shows the contents of an object."""
        if args == "param":
            args = "params"
        try:
            if type(eval("self."+args)) in [dict, list]:
                print(json.dumps(eval("self."+args), indent=4))
            else:
                res = eval("self."+args)
                print(f"{res}")
        except AttributeError:
            print("{}Error 707{}: {}That object has not been set.{}".format(self.Colors.FAIL,
                                                                            self.Colors.ENDC,
                                                                            self.Colors.WARNING,
                                                                            self.Colors.ENDC
                                                                            ))
        except SyntaxError:
            print("{}Error 703{}: {}Invalid object name.{}".format(self.Colors.FAIL,
                                                                   self.Colors.ENDC,
                                                                   self.Colors.WARNING,
                                                                   self.Colors.ENDC
                                                                   ))

    def do_shell(self: object, args):
        """Execute a shell command."""
        self._shell(args)

    def do_store(self: object, args):
        """Stores existing objects into the command array for batch execution."""
        cmd_count = len(self.commands)
        cmd_count += 1
        if args:
            try:
                cmd_action, cmd_name = args.split(" ", 2)
            except ValueError:
                cmd_action = args
                cmd_name = f"Command{cmd_count}"
        else:
            cmd_name = f"Command{cmd_count}"
            cmd_action = "show"

        cmd = {}
        cmd[cmd_name] = {}
        cmd[cmd_name]["params"] = self.params
        cmd[cmd_name]["body"] = self.body
        cmd[cmd_name]["action_name"] = self.action_name
        cmd[cmd_name]["ids"] = self.ids
        cmd[cmd_name]["action"] = cmd_action
        cmd[cmd_name]["returned"] = self.returned

        self.commands.append(cmd)
        print("Command {} ({}{}{}) stored {}successfully{}.".format(cmd_name,
                                                                    self.Colors.BOLD,
                                                                    cmd_action,
                                                                    self.Colors.ENDC,
                                                                    self.Colors.OKGREEN,
                                                                    self.Colors.ENDC
                                                                    ))

    def do_run(self: object, args):
        """Runs commands defined in the commands object."""
        self.result = []
        if args:
            for c in self.commands:
                for key in c:
                    if key.lower() == args.lower():
                        self._api_action(c[key])
        else:
            for c in self.commands:
                for key in c:
                    self._api_action(c[key])

    def do_debugger(self: object, args):
        global debug_started
        if not debug_started:
            from . import _debug as debugger
            debugger.init(creds=self.config)
            debug_started = True
        else:
            from . import _debug as debugger
            importlib.reload(debugger)
            debugger.init(creds=self.config)

    def do_set(self: object, args):
        """Sets the value of an object or a key within an object."""
        try:
            qc = ""
            items = args.split(" ", 3)
            if len(items) > 2:
                elm = items[0]
                key = items[1]
                elm = "params" if elm == "param" else elm
                c = 0
                v = ""
                for item in items:
                    if c > 1:
                        if c == 2:
                            spacer = ""
                        else:
                            spacer = " "
                        v = f"{v}{spacer}{item}"
                    c += 1
                val = v
                exists = False
                try:
                    if hasattr(eval("self."+elm), key):
                        setattr(eval("self."+elm), key, val)
                        exists = True
                    else:
                        pass
                except AttributeError:
                    pass
                try:
                    val = int(val)
                except ValueError:
                    pass
                if str(val).lower() in ['true', 'false']:
                    if val.lower() == "true":
                        val = True
                    else:
                        val = False
                if type(val) not in [dict, bool, int]:
                    qc = "'"
                try:
                    if type(eval("self."+elm)) != dict:
                        exec("self."+elm+" = {}")
                except AttributeError:
                    if not exists:
                        exec("self."+elm+" = {}")
                exec("self."+elm+"[\""+key+"\"]="+qc+str(val)+qc)
                print(f"{key} set to {val} in {elm} object.")
            else:
                elm, val = args.split(" ", 2)
                if "ids" not in elm:
                    try:
                        val = int(val)
                    except ValueError:
                        pass
                if str(val).lower() in ['true', 'false']:
                    if val.lower() == "true":
                        val = True
                    else:
                        val = False
                if type(val) not in [dict, bool, int]:
                    qc = "'"
                print(qc)
                exec("self."+elm+" = "+qc+str(val)+qc)
                print(f"{elm} object set to {val}.")
            if elm.lower() == "active_debug":
                if val:
                    logger.addHandler(ch)
                else:
                    logger.removeHandler(ch)
        except Exception as e:
            err = str(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            msg = "{}Exception {} was generated on line {} in {}{}: {}\n".format(self.Colors.FAIL,
                                                                                 exc_type.__name__,
                                                                                 exc_tb.tb_lineno,
                                                                                 fname,
                                                                                 self.Colors.ENDC,
                                                                                 err
                                                                                 )
            del(exc_type, exc_obj, exc_tb)
            print(msg)
            print("Command format: {}command{} {}item{} (key) {}value{}".format(self.Colors.UNDERLINE,
                                                                                self.Colors.ENDC,
                                                                                self.Colors.BOLD,
                                                                                self.Colors.ENDC,
                                                                                self.Colors.BOLD,
                                                                                self.Colors.ENDC
                                                                                ))


def init():
    """Initializes FalconShell """
    app = Console()
    app._header()
    print("Starting up, please wait...")
    app._load()
    app._connect()
    app.cmdloop(f'Welcome to FalconShell v{_version}!\n')


if __name__ == "__main__":
    init()
