vector = []
may_vec = 0
b = 0
for i in range(5):
    num = int(input("Ingrese un numero: "))
    if b == 0:
        may_vec = num
        b = 1
    else:
        vector.append(num)
        if num > may_vec:
            may_vec = num

print(f"El numero mayor es: {may_vec}")
