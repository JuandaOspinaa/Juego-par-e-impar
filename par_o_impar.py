def verificar_par():
    num = int(input("Ingrese un numero para saber si el numero es par o impar: "))

    if num % 2 == 0:
        print(f'El numero {num} es par.')
    else:
        print(f'El numero {num} es impar.')

while True:
    verificar_par()
    
    try:
        intento = int(input('''Deseas volver a jugar?
              1. Si
              2. No
              Elige una opción: '''))
        
        if intento % 2 == 0:
            print('Gracias por jugar.')
            print('Fin del programa.') 
            break
        elif intento != 1:
            print('Opción inválida. Por favor elige 1 o 2.')
    except ValueError:
        print('Error, Por favor ingrese un número entero.')



            
    
    
