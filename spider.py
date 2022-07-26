# Realizado por Solo a 24/07/20272 última actualización 24/07/2022, WIP


#--------------------------------------------------------------------------------
#-------------------------------LIBRERIAS----------------------------------------

import argparse
from bs4 import BeautifulSoup as bs
import requests
import urllib 

#--------------------------------------------------------------------------------
#-------------------------------VARIABLES----------------------------------------
'''
url = 'ruta no indicada'
nivel = 5
ruta = './data/'
'''
#--------------------------------------------------------------------------------
#--------------------------CONFIGURACION PARSER----------------------------------

parser = argparse.ArgumentParser()
parser.add_argument('-r', help = "Descarga de forma recursiva las imágenes.", action= "store_true")
parser.add_argument('-l', help = "Indica el nivel profundidad máximo de la descarga recursiva", type = int, default = 5)
parser.add_argument('-p', help = "Indica la ruta donde se guardarán los archivos descargados.", type = str, default= "./data/")
# Aqui molaria que si se modifica el path por defecto se fuese la consola, se sacase el nombre de usuario,
# y se hiciese una ruta con mkdir -p para guardar las imagenes rollo /home/$USER/Desktop/aracne (solo en caso de que no haya / en el nombre, que entonces respetamos
# la direccion dada por el usuario, a no ser que no exista, que si no, pues de nuevo se crea una)
parser.add_argument('URL', help = "Indica la web a Scrapear.", type = str)

#--------------------------------------------------------------------------------
#-------------------------------FUNCIONES----------------------------------------






#--------------------------------------------------------------------------------
#-------------------------------EJECUCION----------------------------------------

if __name__ == "__main__":

    args = parser.parse_args()

    print (args.URL)
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    html = requests.get(args.URL, headers=headers)
    
    print (html.status_code)
    soup = bs(html.content, 'html.parser')

    #print(html.status_code)
    imagenes = soup.find_all('img')


    for image in (soup.find_all('img')):
        
        if (image['src'].startswith("https")):
            img = image['src']
            print (image['src'])
            nombre = image['src'].split('/')
            for n in nombre:
                if '.jpg' in n or '.png' in n or '.jpeg' in n or '.gif' in n or '.bmp' in n:
                    n1 = n.split('.')
                    print (n1[0])
            print ('-' * 100)
        
        #img = requests.get(image['src'], headers = headers)
        
        urllib.request.urlretrieve(img, args.p + n1[0])
        '''
        try:
            with open(args.p + '/' + n1[0], "wb") as file:
        
                file.write(img.content)
        except:
            pass
        '''