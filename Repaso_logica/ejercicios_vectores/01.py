A = []
for i in range(10):
    A.append(int(input(f"Ingrese el elemento {i+1}: ")))

N = int(input("Ingrese el número a buscar: "))

contador = 0
for elemento in A:
    if elemento == N:
        contador += 1

print(f"El número {N} aparece {contador} veces en el vector.")
