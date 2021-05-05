#!/usr/bin/python3
import socket as s 
import os, sys

#Autor:Henry Cardenas

def dato_erroneo(): 

    '''Ingresar url sin directorios y sin http
       ejemplo: www.pagina.com
       no:
       www.pagina.com/algo/mas
    '''

    if len(sys.argv) != 2 :
        print("\n[!] Uso: python3 " + sys.argv[0] + " <direccion-url(sin http)>\n")
        sys.exit(1)

    if s.error:
        print('Lo sentimos no se encontro la direccion ip ')

if __name__ == '__main__':

    try:
        url = str(sys.argv[0])
        print(f'La ip de < {url} > es {s.gethostbyname(url)}')
    except:
	dato_erroneo()
