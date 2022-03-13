#!/usr/local/bin/python3
import operator
import sys
'''
 1. For the web server log file "epa-http.txt" provided here - https://github.com/ocatak/apache-http-logs/blob/master/w3af.txt - 
 write a shell/python/ruby script that does the following, across all the requests in the log:
1.a) Print (host, request-count) tuples for the top-10 frequent hosts
1.b) Print (HTTP-status-code, count) tuples, sorted by count
1.c) Print the hour with the highest request count, along with the count
1.d) Print the hour with the highest total number of bytes served, along with the total
1.e) Print the first & last path name components of top-10 most frequently accessed resources
1.f) Print the mean and mode of the distribution of number of GET params
 Write test cases to test your implementation against the log file provided here - http://www.almhuette-raith.at/apache-log/access.log
'''

class LogParse ():
  def __init__(self, fname):
    formatedList = []
    with open(fname, 'r') as fd :
      for line in fd:
        line = line.strip()
        if line == '' :
          continue
                
        time = line.rstrip('"').lstrip('"').split(' ')[3].strip('\[')
        host =  line.rstrip('"').lstrip('"').split(' ')[0]
        method = line.rstrip('"').lstrip('"').split(' ')[5].strip('"')
        resource = line.rstrip('"').lstrip('"').split(' ')[6].strip('\[')
        status_code = line.rstrip('"').lstrip('"').split(' ')[8]
        num_bytes = line.rstrip('"').lstrip('"').split(' ')[9] 
        if num_bytes == '-':
          num_bytes = 0 
        tup =  (host, time, method, resource, status_code, num_bytes)
        formatedList.append(tup)

    self.formatedList = formatedList

  def topTenhostRequestCount (self):
    formatedList = self.formatedList
    count = {}
    for i in formatedList :
      if i[0] in count :
        count[i[0]] += 1
      else :
        count[i[0]] = 1
    
    res = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    #print ( res[0:10] )
    print (' ---- Print (host, request-count) tuples for the top-10 frequent hosts: ----')
    print(res[0:10])
   

  def statusCount (self):
    formatedList = self.formatedList
    count = {}
    for i in formatedList :
      if i[4] in count :
        count[i[4]] += 1
      else :
        count[i[4]] = 1

    res = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    print ("Print (HTTP-status-code, count) tuples, sorted by count")
    print ( res[0:10] )
    

  def requestHourCount(self):
    formatedList = self.formatedList
    count = {}
    for i in formatedList:
      hrs = i[1].split('/')[2].split(':')[1]
      #print (hrs)
      if hrs in count :
        count[hrs] += 1
      else :
        count[hrs] = 1

    res = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    #print (res[0:10])
    print ('Print the hour with the highest request count, along with the count')
    print (res[0])

  def requestByteHourCount(self):
    formatedList = self.formatedList
    count = {}
    for i in formatedList:
      hrs = i[1].split('/')[2].split(':')[1]
      #print (hrs)
      if hrs in count :
        count[hrs] += int(i[5])
      else :
        count[hrs] = int(i[5])

    res = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    #print (res[0:10])
    print ('Print the hour with the highest total number of bytes served, along with the total')
    print(res[0])
   

 # formatedList = parseLogFile(fname)


  def firstAndLastComponet(self):
    formatedList = self.formatedList
    count = {}
    for i in formatedList:
      resource = i[3]
      #print (hrs)
      if resource in count :
        count[resource] += 1
      else :
        count[resource] = 1

    res = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    print ('Print the first & last path name components of top-10 most frequently accessed resources')
    #print (res[0:10])
    for t in res[0:10]:
      u = t[0].split('/')
      if len(u) == 2 and u[0] == '' and u[-1] == '':
        first = 'Null' ; last = 'Null'
      elif len(u) == 2 :    
        first = u[1] ; last = 'Null'
      else  :   
        if u[-1] == '' and len(u) == 3:
          last = 'Null' 
        elif u[-1] == '' and len(u) != 3:
          last = u[-2] 
        else :
          last = u[-1] 
        first = u[1] 
      print('\n')
      print ("first=",first, "last=", last, u)  


def printLineSpace():
  print ('\n' *1, '*' * 80, '\n' *1)

if __name__ == "__main__" :
  if len(sys.argv) < 2 :
    print ('Usage: log_exec.py <fileName> ')
    exit()
  
  fname = sys.argv[1]
  lp = LogParse(fname)
  printLineSpace()

  lp.topTenhostRequestCount()
  printLineSpace()

  lp.statusCount()
  printLineSpace()

  lp.requestHourCount()
  printLineSpace()

  lp.requestByteHourCount()
  printLineSpace()

  lp.firstAndLastComponet()
  printLineSpace()