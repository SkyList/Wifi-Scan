import subprocess
import re


proc = subprocess.Popen('iwlist wlp3s0 scan | grep ESSID', shell=True, stdout=subprocess.PIPE, )
stdout_str = proc.communicate()[0]

arq = open('teste.txt', 'w+')
arq.write(stdout_str)

arq.close()

print (stdout_str)

