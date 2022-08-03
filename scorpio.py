# Realizado por Solo a 02/08/20272 última actualización 03/08/2022 WIP.

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-LIBRERIAS-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

from PIL import Image
from PIL.ExifTags import TAGS
import argparse

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-CONFIGURACION-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

carpeta = 'imgs/'

parser = argparse.ArgumentParser()
parser.add_argument('file_01')
parser.add_argument('file_02', nargs = '*')

args = parser.parse_args()

lista = [args.file_01]
lista = lista + args.file_02

info = {}

for elem in lista:
    info[elem] = {}

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-EJECUCION-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

for clave, valor in info.items():
    
    imagen = carpeta + clave
   
    img = Image.open(imagen)
    exif = img.getexif()

    valor['format'] = img.format
    valor['width'] = img.size[0]
    valor['height'] = img.size[1]
    valor['mode'] = img.mode

    for elem in exif:
        if not isinstance(exif.get(elem), bytes):
            valor[TAGS.get(elem)] = exif.get(elem)
    print ('\033[0;37m' +'-_' * 50, '\n')
    print ('\033[0;36m' +clave +'\n' +'-' * 15 + '\n')
   
    for nombre, dato in valor.items():
        print (f"\033[1;33m     {nombre}: \033[0;32m'{dato}")
