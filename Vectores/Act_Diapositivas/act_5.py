file = open("mbox.txt")
c = 0
for line in file:
    if line.startswith("From"):
        correo = line.split()[1]
        usuario = correo.split('@')[0]
        print(usuario)
        c += 1
        break
print(f"cantidad de lineas 'From': {c}")
