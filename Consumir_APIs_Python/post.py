# %%
import requests

# %%
url = 'http://httpbin.org/post'
payload = {'nombre': 'Flavio', 'curso': 'Python'}
response = requests.post(url, json=payload)
# json = payload ; post internamente se encarga de convertir el diccionario en json
# data = json.dumps(payload) ; nosotros podemos convertir el diccionario en json
if response.status_code == 200:
    content = response.content
    file = open('post.html', 'wb')
    file.write(content)
    file.close()
# %%
