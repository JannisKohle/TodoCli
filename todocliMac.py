#!/usr/bin/env python3

import os
import sys
import json

args = sys.argv[1:]
usage = "Usage: ..."

if len(args) == 0:
    print(usage)

elif args[0] == "db":
    if len(args) != 2:
        print(usage)

    else:
        HOME = os.path.expanduser("~")
        # Create ~/.config/todocli.txt if it doesn't exist already
        if "todocli.txt" not in os.listdir(HOME+"/.config"):
            os.system(f"touch {HOME}/.config/todocli.txt")

        with open(HOME+"/.config/todocli.txt", "r+") as f:
            f.write(args[1])

elif args[0] == "list":
    if args[1] == "create":
        path = args[2]

    elif args[1] == "delete":
        path = args[2]

    elif args[1] == "rename":
        path = args[2]

    elif args[1] == "list":
        path = args[2]

    else:
        print(usage)

elif args[0] == "task":
    if args[1] == "create":
        path = args[2]

    elif args[1] == "delete":
        path = args[2]

    elif args[1] == "edit":
        path = args[2]

    elif args[1] == "list":
        path = args[2]

    else:
        print(usage)

else:
    print(usage)
