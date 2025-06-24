vector = []
contador = 0
suma = 0

for i in range(20):
    vector.append(input("Ingrese un numero: "))  # Agregar el número al vector
    if vector(i) >= 5:  # Comparar el número ingresado, no la lista
        suma += vector(i)  # Sumar el número si cumple la condición
        contador += 1  # Incrementar el contador

print(f"contador: {contador}")
print(f"suma: {suma}")
