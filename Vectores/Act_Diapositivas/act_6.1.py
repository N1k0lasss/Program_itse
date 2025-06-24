lista = list()
while True:
    ingreso = input("Escribe un numero: ")
    if ingreso == "hecho":
        break
    lista.append(int(ingreso))
maximo = max(lista)
minimo = min(lista)
print(f"El maximo es {maximo} y el minimo es {minimo}")
