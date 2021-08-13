import sys
import os
# msg=(sys.argv[1])
(r,w)=os.pipe()
print(r,w)
wid = os.fdopen(w, 'w')
wid.write("Text written by child")
# os.system('py receiver.py '+str(r))
rid = os.fdopen(r, 'r')
str=rid.read(1)
print(str)

