import re
import os

os.system('iwlist interface_de_rede_wifi scanning > res.txt');

'''
ipconfig = subprocess.Popen(['netsh', 'wlan', 'show', 'networks','mode=bssid'],stdout=subprocess.PIPE,)
stdout_str = ipconfig.communicate()[0]

print (stdout_str)

'''
arq = open('res.txt', 'r');
list = arq.readlines();

ssid        = re.findall( r'(ESSID:")([A-z0-9\s]*)' , str(list) );
address     = re.findall( r'(Address:) ([A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9])' , str(list) );
quality     = re.findall( r'(Quality=[0-9][0-9])' , str(list) );
level       = re.findall( r'(level=-[0-9][0-9])' , str(list) );
channel     = re.findall( r'(Channel:[0-9][0-1]?)' , str(list) );
frequency   = re.findall( r'(Frequency:[0-9]*.[0-9]?[0-9]?[0-9]?)' , str(list) );
lastBeacon  = re.findall( r'(beacon: [0-9]*)' , str(list) );


x=0
nElem = len(ssid);

while(x < nElem):
    print('nome - ' + ssid[x][1])
    print('endereço - ' + address[x][1])
    print('qualidade - ' + quality[x].split('=')[1]) 
    print('nivel - ' + level[x].split('=')[1])
    print('canal - ' + channel[x].split(':')[1])
    print('frequencia - ' + frequency[x].split(':')[1])
    print('last beacon - ' + lastBeacon[x].split(':')[1])
    print()
    x+=1

 #   print ( calculateQualityPercent(quality[0].split('=')[1]) ) )

#retorna o valor convertido para porcetagem de base 70
def calculateQualityPercent( quality ):
    number = int(str(quality))
    return (number * 100)/70