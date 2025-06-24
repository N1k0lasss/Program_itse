vectorA = []
vectorB = []

for i in range(5):
    num = int(input("Ingrese el valor del VectorA: "))
    vectorA.append(num)

for i in range(5):
    num = int(input("Ingrese el valor del VectorB: "))
    vectorB.append(num)


def operacion(vectorA, vectorB):
    vectorC = []
    for i in range(len(vectorA)):
        vectorC.append((vectorA[i] * vectorB[i]) // 2)  # División entera
    return vectorC


vectorC = operacion(vectorA, vectorB)
print("VectorC:", vectorC)
