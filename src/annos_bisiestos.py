def evaluar(anno):
    bisiesto = ""
    if anno < 1582:
        if anno % 4 ==0:
            bisiesto = f"{anno} es bisiesto"
        else:
            bisiesto = f"{anno} no es bisiesto"
    elif anno >= 1582:
        if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 ==0):
            bisiesto = f"{anno} es bisiesto"
        else:
            bisiesto = f"{anno} no es bisiesto"
            
    return bisiesto

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
