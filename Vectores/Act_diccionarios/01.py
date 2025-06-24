file = open("Archivos_Clase/words.txt")
diccionario = dict()
for linea in file:
    for palabra in linea.split():
        if not palabra in diccionario:
            diccionario[palabra] = 1
    else:
        diccionario[palabra] += 1

file.close()
print(diccionario)
