# Clases y Objetos

Las clases son un conjunto de objetos que tienen un mismo comportamiento y características. Por ejemplo, si tenemos una clase llamada `Perro`, todos los objetos que pertenezcan a esta clase tendrán las mismas características y comportamientos.

Apartir de las clases podemos crear objetos del mismo tipo, donde cada objeto tendra su propio estado, conservando las mismas características y comportamientos de la clase, pero con estados diferentes. Es decir, cada objeto tendrá sus propios valores para las variables de la clase, pudiendo modificarlos sin afectar a los demás objetos.
Ejemlo de clase:

```python
class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print("Guau Guau")

    def comer(self):
        print("Ñam Ñam")
```

## Terminología

- **Instancia**: Es un objeto creado a partir de una clase.
- **Instanciar**: Es el proceso de crear un objeto a partir de una clase.
- **Estado**: Es el conjunto de valores que tiene un objeto en un momento determinado y que pueden cambiar sin afectar a los demás objetos.
- **Propiedades o atributos**: Son las variables que definen el estado de un objeto.
- **Contexto**: Es el lugar donde se define el estado de un objeto, por lo que cada objeto tiene su propio contexto.

### [Codigo de ejemplo Python](Clases%20y%20Objetos.ipynb)