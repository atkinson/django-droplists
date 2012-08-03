import os
import sys
import urllib2

def urlretrieve(urlfile, fpath):
    chunk = 4096
    f = open(fpath, "w")
    while 1:
        data = urlfile.read(chunk)
        if not data:
            print "done."
            break
        f.write(data)
        print "Read %s bytes"%len(data)