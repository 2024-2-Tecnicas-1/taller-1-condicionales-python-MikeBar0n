def evaluar(dividendo, divisor):
    cociente = dividendo / divisor
    residuo = dividendo % divisor
    if residuo == 0:
        respuesta = f"La división es exacta.\n Cociente: {cociente}\n Residuo: {residuo}"
    else:
        respuesta = f"La división no es exacta.\n Cociente: {cociente}\n Residuo: {residuo}"

    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
