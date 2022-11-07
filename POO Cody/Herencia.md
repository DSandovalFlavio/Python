# Herencia

La herencia es un concepto que nos permite reutilizar código, es decir, que nos permite crear nuevas clases a partir de otras ya existentes. Esto nos permite crear nuevas clases que hereden de otras, y que por lo tanto, tengan todos los atributos y métodos de la clase de la que heredan.

Esto nos da la posibilidad de resolver problemas partiendo de una pensemiento más general, y luego ir haciendo clases más específicas que hereden de la clase general.

La clase general se le conoce como clase padre, y la clase que hereda de la clase padre se le conoce como clase hija.

Tambien nos da la posibilidad de reutilizar codigo al colocar un metodo en una clase padre, y que todas las clases hijas lo hereden.

## Ejemplo

```python
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print("Ñam Ñam")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print("Guau Guau")

```

## Terminología

- **Clase padre**: Es la clase de la que heredan otras clases.
- **Clase hija**: Es la clase que hereda de otra clase.
- **Super**: Es la clase padre de la clase actual.