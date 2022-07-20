# Práctica 7. Programación orientada a objetos. (6 puntos)
## Ejercicio 1 (2 puntos)
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y
DNI. Construye los siguientes métodos para la clase:

● Un constructor, donde los datos pueden estar vacíos.

● Los setters y getters para cada uno de los atributos. Hay que validar las
entradas de datos.

● mostrar(): Muestra los datos de la persona.

● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

### RESPUESTA

class Persona:

    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,edad):
        if edad != int:
            print('Dato incorrecto')
            self.__edad = 0
        else:
            self.__edad = edad
    
    @property
    def DNI(self):
        return self.__DNI


    @DNI.setter
    def DNI(self,DNI):
        self.__DNI = DNI


    def mostrar(self):
        return 'Nombre:', self.nombre, 'Edad:', self.nombre, 'DNI:', self.DNI

    def esMayorDeEdad(self):
        return self.nombre >= 18


## Ejercicio 2 (2 puntos)
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es
una persona) y cantidad (puede tener decimales). El titular será obligatorio y la
cantidad es opcional. Construye los siguientes métodos para la clase:

● Un constructor, donde los datos pueden estar vacíos.

● Los setters y getters para cada uno de los atributos. El atributo no se puede
modificar directamente, sólo ingresando o retirando dinero.

● mostrar(): Muestra los datos de la cuenta.

● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
introducida es negativa, no se hará nada.

● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar
en números rojos.

### RESPUESTA

class Cuenta:

    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.cantidad

    def mostrar(self):
        return 'Titular:', self.titular, 'Cantidad:',self.cantidad
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad

## Ejercicio 3 (2 puntos)
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva
clase Cuenta Joven que deriva de la anterior. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará
expresada en tanto por ciento.Construye los siguientes métodos para la clase:

● Un constructor.

● Los setters y getters para el nuevo atributo.

● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
edad;, por lo tanto hay que crear un método es Titular Válido ( ) que
devuelve verdadero si el titular es mayor de edad pero menor de 25 años y
falso en caso contrario.

● Además la retirada de dinero sólo se podrá hacer si el titular es válido.

● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
bonificación de la cuenta.

● Piensa los métodos heredados de la clase madre que hay que reescribir.

### RESPUESTA

class CuentaJoven(Cuenta):

    def __init__(self,titular,cantidad,bonificacion):
        super().__init__(titular,cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion
    
    def mostrar(self):
        return 'Titular:', self.titular, 'Cantidad:', self.cantidad, 'Bonificacion:', self.bonificacion

    def titularvalido(self):
        return self.titular < 25 and self.titular > 18

    def retirar(self,cantidad):
        if not self.titularvalido():
            print('Retiro denegado')
    
        elif cantidad > 0:
            super().retirar(cantidad)
