file = open("Archivos_Clase/words.txt")
diccionario = dict()

for linea in file:
    for letra in linea:
        if letra.isalpha():
            letra = letra.lower()
            # Usar get para obtener el valor actual o 0
            diccionario[letra] = diccionario.get(letra, 0) + 1

file.close()
print(diccionario)
