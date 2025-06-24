lista = []
while True:
    try:
        numero = int(input("Escribe un numero: "))
        lista.append(numero)
    except ValueError:
        print("Escribe un numero valido")
        break

maximo = max(lista)
minimo = min(lista)
if lista:
    print(f"El maximo es {maximo} y el minimo es {minimo}")
else:
    print("La lista está vacía")

if "hacho" in input("Escribe hecho: "):
    print(f"El maximo es {maximo} y el minimo es {minimo}")
else:
    print("No se ha escrito 'hacho'")
