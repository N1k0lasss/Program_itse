c = 0
a = [0]

for i in range(10):
    a.append(int(input(f"Ingrese un numero {i}: ")))
    n = int(input("Ingrese el numero : "))
    for i in range(5):
        print(f"{n} {i}")
        c += 1
        break
