#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]
usage = "Usage: ..."

if args[0] == "list":
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
