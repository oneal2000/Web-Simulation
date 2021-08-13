import sys
import os
rid = os.fdopen(int(sys.argv[1]), 'r')
str=rid.read()
print(str)
