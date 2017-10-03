from enert import *
import re, sys
import better_exceptions

def err(msg):
    print(msg)
    exit()

def pytef():
    main_usage = """\
Usage: pytef [input_file]
   or: pytef -c|--check
"""
    regex_arg = re.compile(r"^(.*);")
    regex_res = re.compile(r"^.*;(.*)$")

    parser = mkparser(main_usage)
    parser.add_argument("-c", "--check", action="store_true")
    if len(argv) < 2: err(main_usage)
    args = parser.parse_args(argv[1:])
    if args.help: err(main_usage)
    elif args.check:
        Fl("/tmp/.pytef.py").edit()
        exit()
    elif len(args.args) < 1:
        err(main_usage)

    lines = Fl(args.args[0]).linedata()
    if len(lines) == 0: err(main_usage)

    code = ""
    for i in range(0, len(lines)):
        if lines[i][:4] == "from":
            code += lines[i] + "\n"
        elif lines[i][:6] == "import":
            code += lines[i] + "\n"
        elif lines[i][0] == '!':
            func_name = lines[i][1:]
            code += "def test_" + func_name + "():\n"
        elif lines[i][0] == '*':
            code += lines[i][1:] + '\n'
        else:
            arg = regex_arg.findall(lines[i])[0]
            res = regex_res.findall(lines[i])[0]
            code += " "*4 + "assert " + func_name + "(" + arg + ") == " + res + '\n'
    Fl("pytef_out.py").write(code)
    Fl("/tmp/.pytef.py").write(code)
    Shell("py.test pytef_out.py").call()
    Fl("pytef_out.py").rm()
