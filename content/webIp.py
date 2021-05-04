import socket as s 
import os, sys

def dato_erroneo(): 

    if len(sys.argv) != 2 :   
        print("\n[!] Uso: python3 " + sys.argv[0] + " <direccion-url(sin http)>\n")  
        sys.exit(1) 

if __name__ == '__main__':   
    
    try:    
        url = str(sys.argv[0])    
        print(f'La ip de < {url} > es {s.gethostbyname(url)}')    
    except:
