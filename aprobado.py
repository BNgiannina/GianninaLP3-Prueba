#Ejercicio que determine si una estudiante  esta aprobada  o no.
#Autora: Giannina Bernal Navarrete

def determinaraprobado(promedio):
    
    if promedio >= 11:
        resultado = "Aprobado"
    else:
        resultado = "Desaprobado"
    return resultado
promedio = int(input('Ingrese le promedio: '))
print(determinaraprobado(promedio))