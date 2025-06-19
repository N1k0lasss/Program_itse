# Ejemplo de diccionario con tuplas

tupla = {"a": 1, "b": 2, "c": 3}

print(tupla)

# imprimir el valor de la clave "a"
print(tupla["a"])
print(tupla.get("a"))

# fuccion tule()

t = tuple("abc")
print(t)
print(t[0])
print(t[1])
print(t[2])

# operador de comparacion de tuplas
t1 = (1, 2, 3)
t2 = (1, 1, 3)
t3 = (1, 2, 4)

if t1 == t2:
    print("t1 y t2 son iguales")
elif t1 == t3:
    print("t1 y t3 son iguales")
else:
    print("t1 y t3 no son iguales")

# asignacion de tuplas
x = ['pasalo']
y = ['bien']
m = x, y
print(m)
