# link www.google.com.mx
# %%
from ast import arg
import requests

###### Primera Clase ######
# %%
url = 'https://www.google.com.mx'
response = requests.get(url) # hace el request al servidor
print(response.status_code) # imprime el codigo de respuesta
# %%
if response.status_code == 200:
    content = response.content # obtiene el contenido de la pagina
    file = open('google.html', 'wb') 
    file.write(content)
    file.close()
    
###### Segunda Clase ######
# %%
url = 'https://httpbin.org/get'
response = requests.get(url)
if response.status_code == 200:
    content = response.content
    file = open('httpbin.html', 'wb')
    file.write(content)
    file.close()

# Respuesta del servidor
"""{
    "args": {}, 
    "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.27.1", 
        "X-Amzn-Trace-Id": "Root=1-62a77f61-5a73c7511a9112663d9b064a"
    }, 
    "origin": "189.203.89.122", 
    "url": "https://httpbin.org/get"
}
"""
# Los atributos primarios de la respuesta son: args, headers, origin, url

# %%
# Añadiendo argumentos a la peticion GET
args = {'nombre': 'Flavio', 'curso': 'Python'}
response = requests.get(url, params=args) # se encarga de construir la url con los argumentos
if response.status_code == 200:
    content = response.content
    file = open('httpbin_param.html', 'wb')
    file.write(content)
    file.close()


###### Tercera Clase ######
# %%
# Obtener un JSON
response_json = response.json()
# obtener las llaves del JSON
response_json.keys() # RESULTADO: dict_keys(['args', 'headers', 'origin', 'url'])
response_json['url']
# %%
