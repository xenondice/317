import json
import sys
import system.settings as settings
import system.environment as environment

def main():
    pass

if __name__ == "__main__":
    try:
        environment.setup(sys.argv[1:])
    except SyntaxError as e:
        print("{}\nUse argument --help for more help.".format(e))
        exit(-1)
    main()