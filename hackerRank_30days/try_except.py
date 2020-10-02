#Read a string,S,and print its integer value; if S cannot be
#converted to an integer, print Bad String.

***************************************************************

#!/bin/python3

import sys

try:
    S = int(input().strip())
    print(S)
except ValueError:
    print("Bad String")

