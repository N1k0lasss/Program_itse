file = open("Archivos_Clase/mbox.txt")
diccionario = dict()


for linea in file:
    if linea.startswith("From "):
        correo = linea.split()[1]
        diccionario[correo] = diccionario.get(correo, 0) + 1

mayor = None
correo_Mayor = None

for correo, cantidad in diccionario.items():
    if mayor is None or cantidad > mayor:
        mayor = cantidad
        correo_Mayor = correo

print(f"El correo con más mensajes es: {correo_Mayor} con {mayor} mensajes.")
