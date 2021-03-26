"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

_shell.py - FalconShell base class - overrides Cmd class

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
import string
import pydoc
from cmd import Cmd
from ._colors import Colors
from ._constant import egg_carton, header, _version


class FalconShell(Cmd):

    prompt = f"{Colors.BOLD}Falcon>{Colors.ENDC} "
    identchars = string.ascii_letters + string.digits + '_'

    def __init__(self: object) -> object:
        super(FalconShell, self).__init__(completekey="tab")
        self.config = {}
        self.Colors = Colors()
        self.config["debug"] = False
        self.config["active_debug"] = False
        self.falcon = None
        self.cid = None
        self.action_name = None
        self.ids = None
        self.body = {}
        self.params = {}
        self.commands = []
        self.result = []
        self.return_obj = None
        self.returned = None
        self.debug = False
        self.active_debug = False
        self.complete_list = []
        self.debugging = lambda: True if self.debug else False

    def _header(self: object):
        c = 0
        for row in header:
            if c == 1:
                print(row.format(f"{self.Colors.HEADER}"))
            else:
                print(row)
            c += 1
        print(f"{self.Colors.ENDC} ")

    def all_names(self):
        # This method used to pull in base class attributes
        # at a time dir() didn't do it yet.
        lst = dir(self.__class__)
        for x in self.complete_list:
            if "-" not in x:
                lst.append("do_"+x)
        return lst

    def completenames(self, text, *ignored):
        dotext = 'do_'+text
        return [str(a[3:]) for a in self.all_names() if str(dotext) in str(a)]

    def print_topics(self, header, cmds, cmdlen, maxcol):
        m = ""
        if cmds:
            new = []
            for c in cmds:
                if not c == "egg":
                    new.append(c)
            # self.stdout.write("%s\n"%str(header))
            m = m + "%s\n" % str(header)
            if self.ruler:
                # self.stdout.write("%s\n"%str(self.ruler * len(header)))
                m = m + "%s\n" % str(self.ruler * len(header))
            m = m + self.columnize(new, maxcol-1)
            # self.stdout.write("\n")
            m = m + "\n"
        return m

    def _egg(self: object, args):
        print(f"\n\n{self.Colors.DKRED}")
        c = 0
        for egg in egg_carton:
            if c == len(egg_carton) - 1:
                print(egg.format(f"{self.Colors.OKCYAN}FalconShell{self.Colors.ENDC}⠀v{_version}\n\n"))
            else:
                print(egg)
            c += 1

    def do_list_commands(self: object, args):
        """Lists all available API commands. You can search commands for a string by passing it as a parameter.
           \nExample: list_commands aws
        """
        h = 0
        msg = ""
        available = [cm for cm in self.falcon.commands if "-" not in cm[0] and "." not in cm[0]]
        for command in available:
            if args:
                if args.lower() in command[0].lower():
                    h += 1
                    link = command[2].replace("?ids={}", "")
                    c = command[3]
                    msg = msg + f"{self.Colors.BOLD}{command[0]}{self.Colors.ENDC}\n"
                    msg = msg + f"{self.Colors.OKCYAN}{link}{self.Colors.ENDC}\n{c}\n\n"
            else:
                h = 1
                link = command[2].replace("?ids={}", "")
                c = command[3]
                msg = msg + f"{self.Colors.BOLD}{command[0]}{self.Colors.ENDC}\n"
                msg = msg + f"{self.Colors.OKCYAN}{link}{self.Colors.ENDC}\n{c}\n\n"
        if not h:
            msg = msg + f"{self.Colors.FAIL}No matches{self.Colors.ENDC}.\n"
        msg = msg + "\n"
        pydoc.pipepager(msg, cmd='less -F -X -R --quit-if-one-screen')

    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd".'
        if arg:
            # XXX check arg syntax
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n" % str(doc))
                        return
                except AttributeError:
                    # self.stdout.write("%s\n"%str(self.nohelp % (arg,)))
                    # return
                    pass
                # self.stdout.write("%s\n"%str(self.nohelp % (arg,)))
                # Send them to API help instead
                self.do_list_commands(arg)
                return
            func()
        else:
            m = ""
            names = self.get_names()
            cmds_doc = []
            cmds_undoc = []
            help = {}
            for name in names:
                if name[:5] == 'help_':
                    help[name[5:]] = 1
            names.sort()
            # There can be duplicates if routines overridden
            prevname = ''
            for name in names:
                if name[:3] == 'do_':
                    if name == prevname:
                        continue
                    prevname = name
                    cmd = name[3:]
                    if cmd in help:
                        cmds_doc.append(cmd)
                        del help[cmd]
                    elif getattr(self, name).__doc__:
                        cmds_doc.append(cmd)
                    else:
                        cmds_undoc.append(cmd)
            # self.stdout.write("%s\n"%str(self.doc_leader))
            sanitized = [cm for cm in self.complete_list if "-" not in cm and "." not in cm]
            m = m + "%s\n" % str(self.doc_leader)
            m = m + self.print_topics(self.doc_header, cmds_doc, 15, 160)
            m = m + self.print_topics(self.misc_header, list(help.keys()), 15, 160)
            m = m + self.print_topics(self.undoc_header, cmds_undoc, 15, 160)
            # m = m + "Use list_commands to access help for API commands\n\n"
            m = m + self.print_topics("API commands (type list_commands for a complete list)", sanitized, 15, 160)
        pydoc.pipepager(m, cmd="less -F -X -R --quit-if-one-screen")

    def columnize(self, list, displaywidth=80):
        """Display a list of strings as a compact set of columns.
        Each column is only as wide as necessary.
        Columns are separated by two spaces (one was not legible enough).
        """
        if not list:
            # self.stdout.write("<empty>\n")
            return "<empty>\n"

        nonstrings = [i for i in range(len(list))
                      if not isinstance(list[i], str)]
        if nonstrings:
            raise TypeError("list[i] not a string for i in %s"
                            % ", ".join(map(str, nonstrings)))
        size = len(list)
        if size == 1:
            # self.stdout.write('%s\n'%str(list[0]))
            return '%s\n' % str(list[0])
        # Try every row count from 1 upwards
        for nrows in range(1, len(list)):
            ncols = (size+nrows-1) // nrows
            colwidths = []
            totwidth = -2
            for col in range(ncols):
                colwidth = 0
                for row in range(nrows):
                    i = row + nrows*col
                    if i >= size:
                        break
                    x = list[i]
                    colwidth = max(colwidth, len(x))
                colwidths.append(colwidth)
                totwidth += colwidth + 2
                if totwidth > displaywidth:
                    break
            if totwidth <= displaywidth:
                break
        else:
            nrows = len(list)
            ncols = 1
            colwidths = [0]
        m = ""
        for row in range(nrows):
            texts = []
            for col in range(ncols):
                i = row + nrows*col
                if i >= size:
                    x = ""
                else:
                    x = list[i]
                texts.append(x)
            while texts and not texts[-1]:
                del texts[-1]
            for col in range(len(texts)):
                texts[col] = texts[col].ljust(colwidths[col])
            m = m + "%s\n" % str("  ".join(texts))
            # self.stdout.write("%s\n"%str("  ".join(texts)))
        return m
