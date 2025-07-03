# Crear diccionario
persona = {"nombre": "niko", "edad": 21, "ciudad": "Santiago Del Estero"}
vacio = dict()

print(f"Diccionario persona: {persona}")

# Acceso y modificacion
persona["nombre"] = "Tito"
persona["edad"] = 70
persona["ciudad"] = "La banda"
print(f"Valores modificados: {persona}")

# Añadir nueva Clave-Valor
persona['ocupacion'] = "Programador"
print(f"Nueva Clava-Valor: {persona}")

# METODOS
# Numero de pares
print(f"Numero de pares: {len(persona)}")

# si existe en diccionario
if "ciudad" in persona:
    print("la clave existe")
else:
    print("No existe")

# Mostrar keys()
claves = persona.keys()
print(f"Las claves del diccionario son: {list(claves)}")

# Mostrar values()
valores = persona.values()
print(f"Los valores del diccionario son: {list(valores)}")

# Mostar items()
items = persona.items()
print(f"Los items del diccionario son: {list(items)}")

# Get()
# Asignar por defecto
profesion = persona.get('profesion', 'desconocida')
print(f"Profesion {profesion}")
# Obtener ya existente
ocupacion = persona.get('ocupacion')
print(f"Su ocupacion es: {ocupacion}")

# Pop() y Popitem()
edad_eliminada = persona.pop("edad")
print(
    f"Diccionario despues de Pop('edad'): {persona}, edad eliminada: {edad_eliminada}")

ultimo_elemento = persona.popitem()
print(
    f"Diccionario despues del popitem(): {persona}, Ultimo elemento eliminado: {ultimo_elemento}")

# Update()

otro_diccionario = {'email': "tito@gmail.com", 'ciudad': "Capital"}
persona.update(otro_diccionario)
print(f"Diccionario despues del update: {persona}")

# Iteracion sobre el diccionario
# (Itera por claves por defecto)
for clave in persona:
    print(f"clave: {claves}, valor: persona{clave}")
