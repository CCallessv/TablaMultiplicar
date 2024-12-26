contador = 0

def multiplicando():
    global contador
    continuar = True
    print("!Hola :)¡")
    while continuar:
        factor1 = input("Por favor ingrese el numero que desea efectuar la operacion: ")
        if '.' in factor1 or ',' in factor1 or not factor1.isdigit():
            print("Por favor, no ingrese decimales, comillas o letras. Ingrese solo un número entero.")
        else: 
            factor1 = int(factor1)
            contador +=1
            for i in range(1, 11):
                print(f"{factor1} x {i} = {factor1 * i}")      
            continuar_input = input("¿Desea realizar otra operación? (s/n): ").lower()
            if continuar_input != 's':
                continuar = False
    print("Gracias por usar el programa. ¡Hasta luego!") 
 
multiplicando()





