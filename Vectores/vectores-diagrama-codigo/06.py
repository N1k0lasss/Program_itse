vectorA = []
vectorB = []

for i in range(5):
    num = int(input("Ingrese un numero: "))
    vectorA.append(num)

for num in vectorA:
    if num > 0:
        vectorB.append(num)


print("vector A (todos los elementos):", vectorA)
print("vector B (solo elementos positivos):", vectorB)
