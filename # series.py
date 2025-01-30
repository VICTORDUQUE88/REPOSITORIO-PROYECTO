# Victor Gustavo Duque Benalcazar

# Función que genera una serie de números entre un rango específico
def generar_serie_numeros(inicio, fin, paso):
    serie = []
    for numero in range(inicio, fin, paso):
        serie.append(numero)
    return serie
def mostrar_bienvenida():
    nombre_completo = "Victor Gustavo Duque Benalcazar"
    print(f"¡Hola! El autor de este archivo es {nombre_completo}.")
mostrar_bienvenida()
inicio = 1
fin = 20  
paso = 2
serie_numeros = generar_serie_numeros(inicio, fin, paso)
print(f"Serie de números desde {inicio} hasta {fin} con paso {paso}:")
print(serie_numeros)
