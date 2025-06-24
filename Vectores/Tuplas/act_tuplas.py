file = open("Archivos_Clase/romeo.txt")
diccionario = dict()
total_letras = 0

for linea in file:
    for letra in linea:
        if letra.isalpha():
            letra = letra.lower()
            diccionario[letra] = diccionario.get(letra, 0) + 1
            print(f"{letra}: {diccionario[letra]}")
            total_letras += 1

file.close()

for letra, cantidad in diccionario.items():
    porcentaje = (cantidad / total_letras) * 100
    print(f"{letra}: {cantidad} veces, {porcentaje:.2f}%")
