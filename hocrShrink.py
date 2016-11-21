#!/usr/bin/python

import sys, getopt

inputfile = ''
outputfile = ''
div=2
index = 0
f1 = sys.stdin.read()
f2 =sys.stdout

def main(argv):
   global inputfile
   global outputfile
   global div
   global f1
   global index
   global f2
   try:
      opts, args = getopt.getopt(argv,"hi:o:s:",["ifile=","ofile="])
   except getopt.GetoptError:
      print sys.argv[0]+'-i <inputfile> -o <outputfile> -s <shrink-factor>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print sys.argv[0]+'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg   
         f1=open(inputfile,"r").read()
      elif opt in ("-o", "--ofile"):
         outputfile = arg   
         f2=open(outputfile,'w')
      elif opt in ("-s"):
         div = int(arg)
   while index < len(f1):
    if f1[index] == "<":
     #print "Im Tag",index
     while f1[index] != ">":
      #f2.write(f1[index])
      if f1[index:index+4] == 'bbox':
       #print "BBOX gefunden",index
       index+=5
       f2.write('bbox ')
       x1=parseNumber()
       f2.write(str(x1/div)+' ')
       index+=1
       y1=parseNumber()
       f2.write(str(y1/div)+' ')
       index+=1
       x2=parseNumber()
       f2.write(str(x2/div)+' ')
       index+=1
       y2=parseNumber()
       f2.write(str(y2/div)+'')
      #index+=1
      #print "Tag ende",index
      f2.write(f1[index])
      index+=1
    else:
     f2.write(f1[index])
     index+=1
   f2.close()


def parseNumber():
 global index 
 res=0
 while '0' <= f1[index] <= '9':
  res*=10
  res+= ord(f1[index]) - ord('0')
  index += 1
 return res


if __name__ == "__main__":
   main(sys.argv[1:])







