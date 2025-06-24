archivo = open("romeo.txt")
lista = list()
for linea in archivo:
    for palabra in linea.split():
        if palabra not in lista:
            lista.append(palabra)

print(lista)
