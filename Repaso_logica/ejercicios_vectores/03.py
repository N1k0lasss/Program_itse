vector = []
promedio = 0

for i in range(5):
    numero = int(input("Ingrese un numero: "))
    vector.append(numero)

promedio = sum(vector) / len(vector)

mayor_al_promedio = None
if numero > promedio:
    mayor_al_promedio = numero

print(f"numero mayor al promedio es: {mayor_al_promedio}")
