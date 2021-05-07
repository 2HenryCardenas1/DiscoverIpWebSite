#!/usr/bin/python3
# coding : utf-8
import socket as s
import sys
import time

# Autor:Henry Cardenas

def error():
    if len(sys.argv) != 2:
        print("\n[!] Uso: python3 " + sys.argv[0] + " <nombre del dominio>\n")
        sys.exit(1)
    else :
        print("\n\t[x] Lo sentimos, no encontramos la ip")


if __name__ == '__main__':

    try:
        url = str(sys.argv[1])
        print('\n[!] Descifrando host...')
        time.sleep(2)
        print(f'\n\t[*] La ip de < {url} > es {s.gethostbyname(url)}')

    except :
        error()
