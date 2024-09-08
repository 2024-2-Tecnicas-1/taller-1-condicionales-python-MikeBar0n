def evaluar(num_victorias_a, num_victorias_b):
    if num_victorias_a <= 7 and num_victorias_b <= 7:
        if num_victorias_a - num_victorias_b >= 2:
            if num_victorias_a >= 5 and num_victorias_b >= 5:
                resultado = "Ganó A"
            elif num_victorias_a >= 5 and num_victorias_b < 5:
                resultado = "Inválido"
        else:
            resultado = "Aún no termina"
        if num_victorias_b - num_victorias_a >= 2:
            if num_victorias_b >= 5 and num_victorias_a >= 5:
                resultado = "Ganó B"
            elif num_victorias_b >= 5 and num_victorias_a < 5:
                resultado = "Inválido"
        else:
            resultado = "Aún no termina"
    else:
        resultado = "Inválido"

    return resultado

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
