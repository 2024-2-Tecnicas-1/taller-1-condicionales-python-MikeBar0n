def evaluar(a, b, c):
    triangulo = ""
    
    if a > b + c or b > a + c or c > a + b:
        triangulo = "No es un triángulo válido"
    elif a == b == c:
        triangulo = "El triángulo es equilátero"
    elif (a == b and c != a) or (c == b and a != c) or (a == c and a != b):
        triangulo = "El triángulo es isósceles"
    else:
        triangulo = "El triángulo es escaleno"
    
    return triangulo

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
