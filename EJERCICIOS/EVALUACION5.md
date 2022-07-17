# 5 Práctica 5. Operadores relacionales. (6 puntos) 
### 5.1 Ejercicio 1 (2 puntos)
Programa que imprima si el número es positivo o negativo

### Respuesta


numero_posyneg = float(input('Agrega cualquier numero real'))

if numero_posyneg < 0:

    print('El número', numero_posyneg, ' es un número negativo')
    
else:

    print('El número', numero_posyneg, ' es un número positivo')



### 5.2 Ejercicio 2 (2 puntos)
Programa que imprima si el número ingresado esta en el rango de 1 a 7

### Respuesta

num = int(input('Agrega un numero entero'))

if num > 0 and num <= 7:

    print('El numero se encuentra entre el rango del 1 al 7')
    
else:

    print('El número no se encuentra entre el rango del 1 al 7')



### 5.3 Ejercicio 3 (2 puntos)
Programa si el interés es mayor al 30%, sino informa el importe total:

### Respuesta

prestamo = float(input('Agrega el credito que solicitaste'))

if prestamo > 50000:

   print('Interes es mayor al 30%')
   
   prestamo = prestamo*1.32
   
   print('Con un importe total de','$',prestamo)
   
elif prestamo <= 35000 and prestamo <= 20000:

    prestamo = prestamo*1.15
    
    print('El interes es del 15% y con un importe total''$',prestamo)
    
