import requests
import json
from os import system


 
 

 
                             
Nombrechat = input("Escribe el nombre del xat: ")
response = requests.get(f"https://xat.com/web_gear/chat/roomid.php?d={Nombrechat}")

 
xat = response.json()['a']
id = response.json()['id']
descripcion = response.json()['d']

infoxat = xat

separador = ";="


separado = infoxat.split(separador)
print("Id de xat: " + f"{id}")
print("descripción: " + f"{descripcion}")
print("Fondo xat: {}".format(separado[0]))
print("idioma: {}".format(separado[3]))
print("Link radio: {}".format(separado[4]).replace("/;"," "))

