vector_A = []

for i in range(5):
    num = int(input("Ingrese un numero: "))
    vector_A.append(num)

suma = 0
for i in range(len(vector_A)):
    if vector_A[i] != i:
        suma += vector_A[i]

print("Vector A:", vector_A)
print("La suma de los elementos distintos a su índice es:", suma)
