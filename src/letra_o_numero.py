def evaluar(caracter):
    tipo_caracter = ""
    caracter_code = ord(caracter)
    
    if 65 <= caracter_code <= 90:
        tipo_caracter = "Es letra mayúscula"
    elif 97 <= caracter_code <= 122:
        tipo_caracter = "Es letra minúscula"
    elif 48 <= caracter_code <= 157:
        tipo_caracter = "Es número"
    else:
        tipo_caracter = "No es letra ni número"
    
    return tipo_caracter

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
