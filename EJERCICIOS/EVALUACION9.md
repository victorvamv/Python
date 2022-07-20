# Práctica 9. Programación funcional. (6 puntos)
## Ejercicio 1 (2 puntos)
Realice un programa que pregunte aleatoriamente una multiplicación. El programa
debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea
incorrecta el programa debe indicar cuál es la correcta). El programa preguntará
10 multiplicaciones, y al finalizar mostrará el número de aciertos.

#### Análisis
* Hacemos un bucle con 10 iteraciones, en cada iteración se inicializan dos
números con un valor aleatorio (de 2 a 10). Se calcula la multiplicación.
* Mostramos la multiplicación, y pedimos por teclado el resultado. Si
coincide con la multiplicación calculada cuento un acierto, sino escribimos un
mensaje de error mostrando el resultado correcto. Cuando salimos del bucle
mostramos el número de aciertos.

Ejemplo. imprime una multiplicacion (9 * 8 =  )por teclado se ingresa la respuesta, eso pasa 10 veces y al final nos imprime cuantas respuestas fueron correctas

Recuerda el import random

### RESPUESTA


import random


aciertos = 0


for resultado in range(1,11):

    
    num1 = random.randint(2,10)
    num2 = random.randint(2,10)
    print('''multiplica''', num1, '''*''', num2)
    num = num1 * num2
    resultado = int(input('escribe el resultado'))
    if resultado != num:
        print('El resultado', resultado,  'es incorrecto', ', la respuesta correcta es =', num)
    else:
        aciertos = aciertos + 1
        
        print('Respuesta correcta')

print('# de aciertos:', aciertos)


## Ejercicio 2 (2 puntos)
Obtener el cuadrado de todos los elementos en la lista.

### RESPUESTA




  def cuadrado(num):
    return num**2

Lista = [1,2,3,4,5,6,7,8,9,10]

list(map(cuadrado,Lista)


## Ejercicio 3 (2 puntos)
Obtener la cantidad de elementos mayores a 5 en la tupla.

### RESPUESTA




def mayor(numero):
    if numero > 5:
        return True

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)

tuple(filter(mayor, tupla))


## Ejercicio 4 (2 puntos)
Obtener la suma de todos los elementos en la lista

### RESPUESTA



from functools import reduce
def suma(x, y):
      return x + y


lista = [1,2,3,4]

print(reduce(suma, lista))
