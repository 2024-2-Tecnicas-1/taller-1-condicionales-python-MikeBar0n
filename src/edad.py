from time import localtime
def evaluar(dia, mes, anno):
    
    fecha_actual = localtime()
    dia_actual = fecha_actual.tm_mday
    mes_actual = fecha_actual.tm_mon
    anno_actual = fecha_actual.tm_year
    edad = anno_actual - anno

    if mes_actual < mes or (mes_actual == mes and dia_actual < dia):
        edad -= 1

    return f"Usted tiene {edad} años"

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
