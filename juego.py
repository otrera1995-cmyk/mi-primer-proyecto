def saludar(nombre):
    print(f"¡Hola {nombre}!")
    print("Bienvenido al juego de adivinanzas")

def juego():
    numero_secreto = 7
    intentos = 0
    adivinado = False
    
    while not adivinado:
        intento = int(input("Adivina un número entre 1 y 10: "))
        intentos += 1
        
        if intento == numero_secreto:
            print(f"¡¡¡GANASTE!!! en {intentos} intentos")
            adivinado = True
        elif intento < numero_secreto:
            print("El número es MAYOR")
        else:
            print("El número es MENOR")

nombre = input("¿Cuál es tu nombre? ")
saludar(nombre)
juego()

