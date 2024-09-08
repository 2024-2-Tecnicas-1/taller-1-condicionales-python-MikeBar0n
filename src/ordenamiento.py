def evaluar(numero1, numero2, numero3, numero4):
    
    if numero1 > numero2:
        numero1, numero2 = numero2, numero1
    if numero1 > numero3:
        numero1, numero3 = numero3, numero1
    if numero1 > numero4:
        numero1, numero4 = numero4, numero1
    if numero2 > numero3:
        numero2, numero3 = numero3, numero2
    if numero2 > numero4:
        numero2, numero4 = numero4, numero2
    if numero3 > numero4:
        numero3, numero4 = numero4, numero3
    
    return f"{numero1} {numero2} {numero3} {numero4}"

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
