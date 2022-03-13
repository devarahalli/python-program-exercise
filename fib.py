#!/usr/local/bin/python3
import sys

def fib(l):
  init = [1,1]
  for i in range(l):
    init.append(init[len(init)-1] + init[len(init)-2])
  
  print (init[::2])


if __name__ == "__main__" :
  if len (sys.argv) != 2 :
    print ("Usage: ./fib.py 10")
    sys.exit()

  fib(int(sys.argv[1]))
