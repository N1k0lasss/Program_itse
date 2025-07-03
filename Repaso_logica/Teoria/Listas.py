# Todo sobre listas(Arrays o Vectores)

# Creacion de lista

MotosJapones = ["Honda", "Yahama", "Kawasaki", "Suzuki"]
MotosAmericanas = ["Harley-Davidson", "Indian"]
MotosInglesas = ["Triumph", "Royal Enfield"]
MotosItalianas = ["Ducati", "Benelli", "Moto Guzzi", "MV agusta"]

# Acceso por indice
print(f"mostrar elemento: {MotosInglesas[0]}")


# Operaciones Basicas
# concatenacion
allMotos = MotosJapones + MotosAmericanas + MotosInglesas
print(f"lista concatenada{allMotos}")

# repeticion
repeticion = [1, 3, 6, 7, 8, 9] * 2
print(f"Lista repetida{repeticion}")

# rebanado
Sublistas = allMotos[0:4]
print(Sublistas)

# Metodos
# Agregar
MotosJapones.append("caca")
allMotos.extend(MotosItalianas)
print(MotosJapones)
print(allMotos)

# Eliminar
MotosJapones.pop(4)
print(f"Eliminando objeto de lista{MotosJapones}")

# Ordenar
allMotos.sort()
print(f"Lista ordenada{allMotos}")
