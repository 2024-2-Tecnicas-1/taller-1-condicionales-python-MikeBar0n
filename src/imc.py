def evaluar(peso, estatura, edad):
    riesgo = ""
    imc = peso / (estatura ** 2)

    if edad >= 45:
        if imc < 22:
            riesgo = "medio"
        else:
            riesgo = "alto"
    else:
        if imc < 22:
            riesgo = "bajo"
        else:
            riesgo = "medio"
            
    return riesgo

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
