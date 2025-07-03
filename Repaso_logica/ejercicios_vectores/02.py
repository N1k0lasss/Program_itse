vector = []
suma = 0

for i in range(20):
    numero = int(input("Ingrese numero: "))
    vector.append(numero)
    if numero >= 5:
        suma += numero

print(f"Suma de los vectores: {suma}")
print(f"Vector cargado: {vector}")
