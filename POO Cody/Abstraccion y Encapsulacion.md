# Abstraccion y Encapsulacion

## Abstraccion

La abstraccion es el proceso de ocultar los detalles de implementacion y mostrar solo los detalles de uso. Esto nos permite concentrarnos en lo que el objeto hace en lugar de como lo hace.

Ejemplo:

```python
# El telefono es el objeto abstracto ya que no sabemos como funciona internamente
class phone:
    # Estos son los metodos que podemos usar para modificar las propiedades del telefono
    def display_brightness(self):
        # metodo para modificar el brillo de la pantalla
        return 100
    def vibrate(self):
        # metodo para activar la vibracion
        return True
    def sound(self):
        # metodo para activar el sonido
        return True
    def sound_volume(self):
        # metodo para modificar el volumen del sonido
        return 100
    def display(self):
        # metodo para activar la pantalla
        return True
```

## Encapsulacion

Es la habilidad de ocultar la informacion de un objeto de otros objetos. Esto se logra al declarar las variables de instancia como privadas. Esto significa que solo las propias clases pueden acceder a ellas.
La clase envia las propiedades y los metodos en un solo paquete, y no permite que otros objetos accedan directamente a ellos.

### Alcance o scope de las clases

El alcance es la region de un programa donde una propiedad o metodo es accesible. Hay tres tipos de alcance:

- **Publico**: El alcance publico es el alcance por defecto. Las propiedades y metodos publicos son accesibles desde cualquier parte del programa.
- **Protegido**: El alcance protegido es similar al alcance publico, pero las propiedades y metodos protegidos solo son accesibles desde la clase y sus subclases.
- **Privado**: El alcance privado es el mas restrictivo. Las propiedades y metodos privados solo son accesibles desde la clase que los define.

### Como se accede a las propiedades de un objeto

- **Primera opcion**: Se puede acceder a las propiedades dentro de la misma clase usando la palabra reservada **self**.

- **Segunda opcion**: Se puede acceder desde una clase que hereda de la clase que contiene la propiedad.

- **Tercera opcion**: Se puede acceder desde un objeto que instancia la clase que contiene la propiedad.

```python
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.apellido = "Garcia" # propiedad publica
    def saludar(self, saludo):
        print(saludo, self.nombre)
    
class Empleado(Usuario):
    _salario = 1000 # propiedad protegida
    __aguinaldo = 100000 # propiedad privada
    
    def modificar_salario(self, nuevo_salario):
        self._salario = nuevo_salario
    
    def consultar_salario(self):
        return self._salario
    
    def modificar_aguinaldo(self, nuevo_aguinaldo):
        self.__aguinaldo = nuevo_aguinaldo
    
    def consultar_aguinaldo(self):
        return self.__aguinaldo
    
    def saludar(self):
        super().saludar("Hola")
        print("Mi nombre es", self.nombre, "y mi salario es", str(self._salario))

class Ejecutivo(Empleado):
    def saludar(self):
        super().saludar()
        print("Y soy un ejecutivo")
    def bono_mas_aguinaldo(self):
        return self._salario + self.__aguinaldo # no se puede acceder a la propiedad privada desde fuera de la clase, esto generara un error
```

## Metodos accesores

Son metodos que permiten acceder y modificar las propiedades de un objeto. Estos metodos se llaman **getters** y **setters** respectivamente. Esto permite que las propiedades sean privadas y solo se puedan acceder a ellas a traves de los metodos que implementan validaciones antes de modificarlas.

```python
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.apellido = "Garcia"
        self.__edad = 0
    def saludar(self, saludo):
        print(saludo, self.nombre)
    
    @property
    def edad(self): # getter
        return self.__edad
    
    @edad.setter
    def edad(self, edad): # setter
        if edad < 0:
            self.__edad = 0
        else:
            self.__edad = edad
```

El concenso es que los metodos **getters** y **setters** se llaman igual que la propiedad que modifican, pero en minusculas. Esto es para que sea mas facil identificar que son metodos y no propiedades.

## Diferencias entre abstraccion y encapsulacion

- La abstraccion es el proceso de ocultar los detalles de implementacion y mostrar solo los detalles de uso. Esto nos permite concentrarnos en lo que el objeto hace en lugar de como lo hace.
- Encapsulacion es la habilidad de ocultar la informacion de un objeto de otros objetos. Esto se logra al declarar las variables de instancia como privadas. Esto significa que solo las propias clases pueden acceder a ellas.
