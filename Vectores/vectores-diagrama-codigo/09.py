edad = []
menores_de_12 = []
entre_13_16 = []
entre_17_20 = []
mayores_de_20 = []
mayor = 0
menor = 0

for i in range(10):
    edad.append(int(input("Ingrese la edad del alumno: ")))

for i in range(10):
    if i == 0:
        mayor = edad[i]
        menor = edad[i]
    else:
        if edad[i] > mayor:
            mayor = edad[i]
        if edad[i] < menor:
            menor = edad[i]

    if edad[i] < 12:
        menores_de_12.append(edad[i])
    elif edad[i] >= 13 and edad[i] < 16:
        entre_13_16.append(edad[i])
    elif edad[i] >= 17 and edad[i] < 20:
        entre_17_20.append(edad[i])
    elif edad[i] >= 20:
        mayores_de_20.append(edad[i])


print("Edades menores de 12:", menores_de_12)
print("Edades entre 13 y 16:", entre_13_16)
print("Edades entre 17 y 20:", entre_17_20)
print("Edades mayores de 20:", mayores_de_20)
print("el alumno Mayor es :", mayor)
print("el alumno Menor es :", menor)
