"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
import random                            #se importa la libreria random
import string                           # se importa la libreria string
from palabras import palabras          # se trae la libreria palabras y se importa la variable palabras
from ahorcado_diagramas import vidas_diccionario_visual  # del archivo ahorcado_diagrama se trae el diccionario donde se tienen las opciones


def obtener_palabra_válida(palabras):   # se crea la funcion para obtener una palabra al azar
    palabra = random.choice(palabras)   # se crea la variable para que se elija de forma aleatoria una palabra de la variable palabras


    while '-' in palabra or ' ' in palabra:    # while para escoger seguir escogiendo la palabra de forma aleatoria
        palabra = random.choice(palabras)      # variable en donde se buscara un valor de la lista plabras

    return palabra.upper()                     # volvera la plabra pero cada letra en mayuscula


def ahorcado():                                 # funcion llamada ahorcado 

    print("=======================================")      # se imprime mensaje al jugador
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)        # se crean todas las variables donde se guardaran el progreso del juego del ahorcado
    letras_por_adivinar = set(palabra)  
    abecedario = set(string.ascii_uppercase)          # variable de un conjunto set 
    letras_adivinadas = set()                         # variable  en las que se guardaran las letras adivinadas

    vidas = 7                   # funcion del número de vidas que se tiene


    while len(letras_por_adivinar) > 0 and vidas > 0:               # se termina el juego cuando las vidas lleguen a cero 

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")   # se imprime le número de vidas que quedan y las letras que has usado

      
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) 
        print(f"Palabra: {' '.join(palabra_lista)}") 

     
        letra_usuario = input('Escoge una letra: ').upper()  # se pide un aletra por teclado y se trasnformara todo en mayuscula

        if letra_usuario in abecedario - letras_adivinadas:  
            letras_adivinadas.add(letra_usuario)            # se añade elementos si es que adivinaste la letra
       
            if letra_usuario in letras_por_adivinar:         
                letras_por_adivinar.remove(letra_usuario)
                print('')
         
            else:                         
                vidas = vidas - 1                                             # sino adivinaste la palabra te resta una vida
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")  # se imprime al usuario que no se encontro la letra
        
        elif letra_usuario in letras_adivinadas:                                   # 
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")   # se imprime si ya escogiste la letra      
        else:
            print("\nEsta letra no es válida.")                                    # si ingresas un valor no valido se dara un aviso

   
    if vidas == 0:                                                                   # si las vidas llegan a cero
        print(vidas_diccionario_visual[vidas])                                       # se imprime del archivo ejecutable vidas_diccionario_visual el resultado
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")    # se imprime el anuncio que perdiste y te dan la palabra que tenias que adivinar
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')                     # en todo caso solo se imprimira un aviso que se adivino la palabra


    ahorcado()                                                               # se trae la funcion ahorcado
