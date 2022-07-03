# Taller consumir APIs con Python

Consumiendo APIs con Python para crear clientes,crear peticiones y enviarlas a los servidores, curso enfocado del lado del cliente.

## Que es una API?

El término API es una abreviatura de Application Programming Interfaces, que en español significa interfaz de programación de aplicaciones. Se trata de un conjunto de definiciones y protocolos que se utiliza para desarrollar e integrar el software de las aplicaciones, permitiendo la comunicación entre dos aplicaciones de software a través de un conjunto de reglas.

## Request

Es una biblioteca HTTP elegante y simple para Python [Link](https://requests.readthedocs.io/en/latest/#)

## Metodos

- [**GET**](./get.py) : Este método permite buscar información/datos según el recurso y el punto final introducido. A través de este método, el backend devolverá la información consultada.
  - **Args** Si quisieramos agregar parametros en la url, podemos hacerlo añadiendo argumentos a la funcion `get(url, params)` y esta se encarga de construir la url.

- [**POST**](./post.py) (Data sending/loading)  :Crear/ejecutar un montón de nueva información en la base. Es necesario enviar la información en la norma JSON requerida en el cuerpo de la solicitud.
  - **Json / Data** : Para enviar datos en formato JSON, podemos utilizar la función `json.dumps(payload)` para convertir el dict en un json o `json = payload` para enviar el dict directamente.

- [**HEADER**](./header.py) :

- **PUT** (Actualización de datos) :
Se utiliza para actualizar o editar la información que ya existe en la base. Algunos API contemplan o no el uso de Patch (indicado para actualizaciones parciales), y el uso de Put es ampliamente conocido y el responsable de cambiar/actualizar la información existente.

- **DELETE** (Borrar datos) :
Como su nombre indica, es el método responsable de borrar la información. Se trata de un punto importante que sólo se incluye en la API si, para la regla de negocio, es necesario excluir información de la base (y si está permitido). Algunas empresas no permiten este uso, porque es una acción que borrará definitivamente el registro particular.

## Respuestas

Normalmente se genera una respuesta en formato JSON.

Todo servidor tiene la obligacion de devolvernos un status de nuestra peticion como un valor numerico.

Cuando se realiza una petición determinada, es de vital importancia conocer si dicha operación se ha llevado a cabo de manera satisfactoria o por el contrario se ha producido algún tipo de error. Para ello, HTTP dispone de un amplio número de códigos de error/éxito ([link info](https://es.wikipedia.org/wiki/Anexo:C%C3%B3digos_de_estado_HTTP)) que cubren todas las posibles respuestas que el usuario puede recibir cuando trata de manipular un recurso mediante el uso de una API REST.

Valores:

## GET

