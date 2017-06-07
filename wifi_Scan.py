import re
import subprocess


'''
ipconfig = subprocess.Popen(['netsh', 'wlan', 'show', 'networks','mode=bssid'],stdout=subprocess.PIPE,)
stdout_str = ipconfig.communicate()[0]

print (stdout_str)

'''
arq = open('res.txt', 'r');
list = arq.readlines();

ssid        = re.findall( r'(ESSID:["])([A-z0-9_]*[^"])*' , str(list) );
address     = re.findall( r'(Address:) ([A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9])' , str(list) );
quality     = re.findall( r'(Quality=[0-9][0-9])' , str(list) );
level       = re.findall( r'(level=-[0-9][0-9])' , str(list) );
channel     = re.findall( r'(Channel:[0-9][0-1]?)' , str(list) );
frequency   = re.findall( r'(Frequency:[0-9]*.[0-9]?[0-9]?[0-9]?)' , str(list) );
lastBeacon  = re.findall( r'(beacon: [0-9]*)' , str(list) );



x=0
nElem = len(ssid);
while(x < nElem):
    print(ssid[x])
    print(address[x])
    print(quality[x])
    print(level[x])
    print(channel[x])
    print(frequency[x])
    print(lastBeacon[x])
    x+=1