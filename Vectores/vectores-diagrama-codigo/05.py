vector = []
suma_vector = 0

for i in range(20):

    vector.append(int(input("Ingrese un numero: ")))
    if vector[i] % 2 == 0:
        suma_vector += vector[i]
        print(f"El numero {vector[i]} es par")
    else:
        print(f"El numero {vector[i]} es impar")
print(f"La suma de los numeros pares es {suma_vector}")
