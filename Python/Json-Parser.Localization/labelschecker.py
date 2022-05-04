#coding:utf-8 
import sys
import tracemalloc

print(len(sys.argv))
if len(sys.argv) < 3:
  print("== YOU MUST CREATE TWO FILES!  ==")
  print("= 1. Source file!")
  print("= 2. Output file!")
  print("This script will delete the same line in same file.")
  sys.exit(0)

print("===== WELCOME TO LABELS CHECKER! =====")
readDir = sys.argv[1]
writeDir = sys.argv[2] 
lines_seen = set() 
outfile=open(writeDir,"w") 
f = open(readDir,"r") 
for line in f: 
  if line not in lines_seen: 
    outfile.write(line) 
    lines_seen.add(line)
    print("Keep line: "+line)
outfile.close() 
print("oh yeah")
