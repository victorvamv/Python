# Práctica 4. 6 puntos
## Tipos de colección de datos.
### 4.1 Ejercicio 1(1.2 puntos)
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su
cuadrado y su cubo.
Respuesta:

import random

numero = []

cubo = []

cuadrado = []



num_cont = 0

numero_aleatorio = 0


while num_cont < 10:

    numero_aleatorio = random.randint(1, 10)
    
    num_cont = num_cont + 1
    
    numero.append(numero_aleatorio)
    
    numero_cuadrado = numero_aleatorio**2
    
    cuadrado.append(numero_cuadrado)
    
    numero_cubo = numero_aleatorio**3
    
    cubo.append(numero_cubo)
    


print('1° número aleatorio',numero[0], ', elevado al cuadrado =', cuadrado[0], ' y elevado al cubo =', cubo[0])

print('2° número aleatorio',numero[1], ', elevado al cuadrado =', cuadrado[1], ' y elevado al cubo =', cubo[1])

print('3° número aleatorio',numero[2], ', elevado al cuadrado =', cuadrado[2], ' y elevado al cubo =', cubo[2])

print('4° número aleatorio',numero[3], ', elevado al cuadrado =', cuadrado[3], ' y elevado al cubo =', cubo[3])

print('5° número aleatorio',numero[4], ', elevado al cuadrado =', cuadrado[4], ' y elevado al cubo =', cubo[4])

print('6° número aleatorio',numero[5], ', elevado al cuadrado =', cuadrado[5], ' y elevado al cubo =', cubo[5])

print('7° número aleatorio',numero[6], ', elevado al cuadrado =', cuadrado[6], ' y elevado al cubo =', cubo[6])

print('8° número aleatorio',numero[7], ', elevado al cuadrado =', cuadrado[7], ' y elevado al cubo =', cubo[7])

print('9° número aleatorio',numero[8], ', elevado al cuadrado =', cuadrado[8], ' y elevado al cubo =', cubo[8])

print('10° número aleatorio',numero[9], ', elevado al cuadrado =', cuadrado[9], ' y elevado al cubo =', cubo[9])




### 4.2 Ejercicio 2 (1.2 puntos)
Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia
los elementos de la lista en otra lista pero en orden inverso, y muestra sus
elementos por la pantalla.

cadena = []

cadena_123 = []

cadena_cont = 0



while cadena_cont < 5:

    cadena_cont = cadena_cont + 1
    

    cad = input('AGREGA LO QUE QUIERAS ')
    
    cadena.append(cad)
    
    cadena_123 = cadena[::-1]
    


print(cadena_123)


### 4.3 Ejercicio 3 (1.2 puntos)
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas,
la nota media, la nota más alta que ha sacado y la menor.

notas_1 = []

nota_cont = 0

num = 0

media = 0


while nota_cont < 5:

    nota_cont = nota_cont + 1
    
    num = int(input('Agrega tus 5 notas calificadas del 0 al 10'))
    

    notas_1.append(num)
    
    media = media + num
    
media = media/nota_cont


print('Total de notas :', notas_1)

print('La nota maxima del alumno fue:', max(notas_1))

print('La nota minima que obtuvo el alumno fue:', min(notas_1))

print('El promedio total =', media)




### 4.4 Ejercicio 4 (1.2 puntos)
Codifica un programa en python que nos permita guardar los nombres de los
alumnos de una clase y las notas que han obtenido. Cada alumno puede tener
distinta cantidad de notas. Guarda la información en un diccionario cuya claves
serán los nombres de los alumnos y los valores serán listados con las notas de
cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su
nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al
final el programa nos mostrará la lista de alumnos y la nota media obtenida por
cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el
programa nos dará un error.

grupo = {}

alumnos = []



cantidad_alumnos = int(input('¿Cuantos alumnos vas agregar?'))

for num in range(cantidad_alumnos):


    alumnos = input('Introduce el nombre del alumno')
    

    notas = []
    
    nota = int(input('Ingresa la nota del alumno'))
    

    while nota > -1:

        notas.append(nota)
        
        nota = int(input('Ingresa la nota del alumno'))
        

    grupo[alumnos] = notas.copy()


for alumnos, notas in grupo.items():


    print('Alumno:', alumnos, 'Total de notas:',
    
          notas, 'Promedio', sum(notas)/len(notas))
          


### 4.5 Ejercicio 5 (1.2 puntos)
Crea una tupla con los meses del año, pide números al usuario, si el número está
entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
muestra un mensaje de error. El programa termina cuando el usuario introduce un
cero.


meses = 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'


numero_usuario = int(input('agrega un número: puedes incluir el 0'))


print(meses[numero_usuario])


# TRATA DE RESOLVER Y AVANZAR LO MÁS POSIBLE EN LOS EJERICICIOS, EL MARTES HABILITO "AYUDAS" EN CADA EJERCICIO
