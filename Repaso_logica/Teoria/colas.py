# concepto FIFO
# Primero en entrar Primero en salir

# Crear colavacia
cola = []

# Encolar
# Añade elemento al final
cola.append("vako")
cola.append("pulgon")

# Desencolar
# Elimina el primera elemento
fifo = cola.pop(0)
print(f"First in First out: {fifo}")
