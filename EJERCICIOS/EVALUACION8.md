# Práctica 8. (6 puntos)
## Ejercicio 1 (2 puntos)
Escribe un programa python que pida un número por teclado y que cree un
diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los
valores sean los cuadrados de las claves.

Ejemplo: si se ingresa el 4 imprima el cuadrado de 1, de 2, de 3 y de 4

num = int(input('ingresa un número entero'))

dic_num = {}

for cuadrado in range(1,num+1):

    dic_num[cuadrado] = cuadrado*cuadrado
    
for cuadrado, x in dic_num.items():

    print("%d = %d" % (cuadrado,x))


## Ejercicio 2 (2 puntos)
Escribe un programa que lea una cadena y devuelva un diccionario con la
cantidad de apariciones de cada carácter en la cadena.

Ejemplo: si se ingresa "paloma" p=1 a=1 l=1 o=1 m=1


 dic_texto = {}

 texto = input("Escribe una palabra")


 for text in texto:

    if text in dic_texto:
    
        dic_texto[text] += 1
        
    else: 
    
        dic_texto[text] = 1

 for x,y in dic_texto.items():

    print(x,"=",y)


## Ejercicio 3 (2 puntos)
Vamos a crear un programa en python donde vamos a declarar un diccionario para
guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta
y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de
los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras
cada consulta el programa nos preguntará si queremos hacer otra consulta.

frutas = {"uvas":20, "kiwi":40, "platano":25, "tuna": 20}

while True:

    fruta = input('Ingresa una fruta que se haya vendido')
    
    if fruta.lower() not in frutas:
    
        print('La fruta no se encuentra')
        
    else:
    
        kg = float(input('cuantos kg se han vendido'))
        
        total = kg*frutas[fruta]
        
        print('El precio total es =', total)
        
    fruta_2 = input('¿Se ha vendido otra fruta? (s/n)')
    
    while fruta_2.lower() != "s" and fruta_2.lower() != "n":
    
        fruta_2 = input('¿Se ha vendido otra fruta? (s/n)')
        
    if fruta_2.lower() == 'n':
    
        break
