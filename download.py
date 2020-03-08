import os
import subprocess

def __external_cmd(cmd, code="utf8"):
  print(cmd)
  process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  while process.poll() is None:
    line = process.stdout.readline()
    line = line.strip()
    if line:
      print(line.decode(code, 'ignore'))

file = open('link.txt')  

with open('link.txt','r', encoding='UTF-8') as f:
    line = f.readline()
    while line:
        print(line.strip('\n'))
        __external_cmd("you-get " + line.strip('\n') + " --debug")
        line = f.readline()
        
