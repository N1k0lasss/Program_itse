file = open("Archivos_Clase/words.txt")
diccionario = dict()

for linea in file:
    for letra in linea:
        if letra.isalpha():
            if letra not in diccionario:
                diccionario[letra] = 1
            else:
                diccionario[letra] += 1

file.close()
print(diccionario)
