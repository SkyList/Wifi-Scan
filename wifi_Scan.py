import re
import os
import time

#METODO QUE RETORNA O VALOR EM PORCENTAGEM, NA BASE 70
def calculateQualityPercent( quality ):
    number = int(str(quality))
    return (number * 100)/70

#LÊ O ARQUIVO E ARMAZENA O TEXTO EM UMA LISTA
def fileHandler( name ):
    arq = open( name+'.txt', 'r');
    list = arq.readlines();

#PEGA  AS SAIDAS DO TERMINAL E JOGA EM UM ARQUIVO DE TEXTO
def callCmd( interface ):
    os.system('iwlist '+ interface+' scanning > res.txt');

def __main__():
    while(True):
        #callCmd( 'Nome da interface' );
        fileHandler('res');
        #SEPARA A LEITURA FEITA DO ARQUIVO COM REGEX EM VARIAS LISTAS 
        ssid        = re.findall( r'(ESSID:")([A-z0-9\s]*)' , str(list) );
        address     = re.findall( r'(Address:) ([A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9]:[A-Z0-9][A-Z0-9])' , str(list) );
        quality     = re.findall( r'(Quality=[0-9][0-9])' , str(list) );
        level       = re.findall( r'(level=-[0-9][0-9])' , str(list) );
        channel     = re.findall( r'(Channel:[0-9][0-1]?)' , str(list) );
        frequency   = re.findall( r'(Frequency:[0-9]*.[0-9]?[0-9]?[0-9]?)' , str(list) );
        lastBeacon  = re.findall( r'(beacon: [0-9]*)' , str(list) );

        #APRESENTA OS VALORES NA TELA, MAS PODE SER USADO PARA MONTAR O COMANDO SQL E ENVIAR PARA O SERVIDOR
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

        # A CADA UM MINUTO REFAZ TODO O PROCESSO
        time.sleep(60);


__main__();