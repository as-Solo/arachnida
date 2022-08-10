# Realizado por Solo a 24/07/20272 última actualización 30/07/2022.


#--------------------------------------------------------------------------------------------------------
#-----------------------------------------LIBRERIAS------------------------------------------------------

import argparse
from bs4 import BeautifulSoup as bs
import requests
import base64
import random
import os

#--------------------------------------------------------------------------------------------------------
#---------------------------------------CONFIGURACION----------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument('-r', help = "Descarga de forma recursiva las imágenes.", action= "store_true")
parser.add_argument('-l', help = "Indica el nivel profundidad máximo de la descarga recursiva", type = int, default = 5)
parser.add_argument('-p', help = "Indica la ruta donde se guardarán los archivos descargados.", type = str, default= "./data/")
parser.add_argument('URL', help = "Indica la web a Scrapear.", type = str)

args = parser.parse_args()

if args.URL.startswith('www'):
    args.URL = 'https://' + args.URL

cmd = 'whoami'
user = os.popen(cmd).read()[:-1]
if args.p != "./data/":
    if  args.p.startswith('/'):
        os.system (f'mkdir -p .{args.p}')
        args.p = '.' + args.p.rstrip('/')
    else:
        os.system (f'mkdir -p ~/Desktop/{args.p}')
        args.p = '/home/' + user + '/Desktop/' + args.p.rstrip('/')

if args.r != True:
    args.l = 1

print ('*' * 25, args.p, '*' * 25, args.l)
#--------------------------------------------------------------------------------------------------------
#-----------------------------------------VARIABLES------------------------------------------------------

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

images_data = []

#--------------------------------------------------------------------------------------------------------
#-----------------------------------------FUNCIONES------------------------------------------------------

def insertar_url (lista, lista2, url, url_base):
    
    
    if url.startswith('/'):
        url = url_base + url

    if confirm_url:
        if url.startswith ('#') or url.startswith ('?'):
            print ('desechado', '-' * 15 , url)
        elif url.startswith(url_base):
            if url.endswith('/'):
                url = url[:-1]
            if url in lista or url in lista2:
                print ('duplicado', '-' * 15 , url)
            elif url not in lista and url not in lista2:
                lista.append(url)
    

def confirm_url (url):
    try:
        chivato = requests.get(url, headers= headers)
        print (chivato.status_code)
        if chivato.status_code == 200:
            return True
    except:
        return False


def name_url (img_src):
    
    img = ["Error al descargar la imagen", "https://w7.pngwing.com/pngs/436/575/png-transparent-computer-icons-error-checklist-trademark-area-warning.png"]
    
    if img_src.startswith("data:image"):
        
        data = img_src.split(',')
        if data[1] not in images_data:
            images_data.append(data[1])
            img[1] = base64.b64decode(data[1])
            if 'jpg' in data[0]:
                img[0] = 'logo_' + str(random.randint(0,100)).zfill(3) + '.jpg'
            elif 'jpeg' in data[0]:
                img[0] = 'logo_' + str(random.randint(0,100)).zfill(3) + '.jpeg'
            elif 'png' in data[0]:
                img[0] = 'logo_' + str(random.randint(0,100)).zfill(3) + '.png'
            elif 'gif' in data[0]:
                img[0] = 'logo_' + str(random.randint(0,100)).zfill(3) + '.gif'
            elif 'bmp' in data[0]:
                img[0] = 'logo_' + str(random.randint(0,100)).zfill(3) + '.png'
    
    
    elif img_src.startswith("https"):
        
        img[1] = requests.get(img_src, headers = headers).content
        nombre = image['src'].split('/')
        for n in nombre:
            if '.jpg' in n:
                n1 = n.split('.')
                img[0] = n1[0] + '.jpg'
            elif '.jpeg' in n:
                n1 = n.split('.')
                img[0] = n1[0] + '.jpeg'
            elif '.png' in n:
                n1 = n.split('.')
                img[0] = n1[0] + '.png'
            elif '.gif' in n:
                n1 = n.split('.')
                img[0] = n1[0] + '.gif'
            elif '.bmp' in n:
                n1 = n.split('.')
                img[0] = n1[0] + '.png'
    return (img)

#--------------------------------------------------------------------------------------------------------
#-----------------------------------------EJECUCION------------------------------------------------------

if confirm_url(args.URL):
    url_a_scrapear = [args.URL.rstrip('/')]
    url_total = [args.URL.rstrip('/')]
    url_base = (args.URL.split('/')[0] + '//' + args.URL.split('/')[2])
else:
    url_a_scrapear = []
    url_total = []
    print (f"{args.URL} no es una dirección válida.")


while args.l > 1:
    
    url_aux = []
    for url in url_a_scrapear:
    
        try:
            html = requests.get(url, headers= headers)
            soup = bs(html.content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                insertar_url (url_aux, url_total, link['href'], url_base)
        except:
            pass


    args.l -= 1
    url_total = url_total + url_aux
    url_a_scrapear = url_aux


for elem in url_total:
    htmli = requests.get(elem, headers = headers)
    
    #print (htmli.status_code)
    soupi = bs(htmli.content, 'html.parser')

    imagenes = soupi.find_all('img')

    for image in (soupi.find_all('img')):
        
        
        img = image['src']
        
        #print ('-' * 25, image['src'], '-' * 25)
        nu = name_url(img)
        try:
            with open(args.p + '/' + nu[0], "wb") as file:    
                file.write(nu[1])
        except:
            pass