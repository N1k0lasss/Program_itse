vector = []
prom = 0
sum1 = 0
cont = 0
for i in range(5):
    vector.append(int(input("Digite um numero: ")))
    sum1 = sum1 + vector[i]
    cont = cont + 1
prom = sum1 / cont
print("el promedio es:", prom)
for i in range(5):
    if vector[i] > prom:
        print("mayores al promedio:", vector[i])
