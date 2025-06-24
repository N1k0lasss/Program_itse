vector = []

for i in range(5):
    num = int(input("Ingrese un numero: "))
    vector.append(num)

promedio = sum(vector) / len(vector)

mayor_al_promedio = None
for num in vector:
    if num > promedio:
        mayor_al_promedio = num

print("elementos del vector:", vector)
print("El mayor al promedio es:", mayor_al_promedio)
print("El promedio es:", promedio)
