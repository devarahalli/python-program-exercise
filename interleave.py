#!/usr/local/bin/python3
from itertools import islice
import os, sys


def fileCleanUp(fName):
    tf = fName + 'temp'
    cmd = 'grep -v -e \'^$\'' + ' ' + fName + ' > ' + tf  
    os.system(cmd)
    return tf

def interFile (N, *fl):
  # number of sequential lines to read from each file
  fl = fl[0]
  N = int(N)

  #import pdb; pdb.set_trace()
  fl_temp = []
  for i in fl:
    tf = fileCleanUp(i)
    fl_temp.append(tf)
  
  print (fl_temp)
  
  files = [open(n) for n in fl_temp]
  
  line = ''.join([''.join(islice(f, N)) for f in files])[:-1]
  while line:
      print(line)
      line = ''.join([''.join(islice(f, N)) for f in files])[:-1]
  
  [f.close() for f in files]
  [os.remove(f) for f in fl_temp ]
  
if __name__ == '__main__':
  if len (sys.argv) != 5 :
    print ("Usage: <ScriptName> <InteleaveNumber> <File1> <File2> <File3>")
    sys.exit()
  
  interFile(sys.argv[1], sys.argv[2:])
