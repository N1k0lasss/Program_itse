vector = []
may_vec = 0
b = 0
for i in range(5):
    num = int(input("Ingrese un número: "))
    if b == 0:
        may_vec = num
        b = 1
    else:
        vector.append(num)
        if num > may_vec:
            may_vec = num

print(f"El mayor número ingresado es: {may_vec}")
