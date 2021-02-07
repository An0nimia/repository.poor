#!/usr/bin/python3

from hashlib import md5
f1 = open("addons.xml", "rb")
buffer1 = f1.read()
f1.close()
hashh = md5(buffer1).hexdigest()
f2 = open("addons.xml.md5", "w")
buffer2 = f2.write(hashh)
f2.close()