"""- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""

usuario={"nombre": " ", "apellidos":"  ","edad": 0, "dni": " "}
usuario["nombre"] = input("Ingrese su nombre: ")
usuario["apellidos"] = input("Ingrese sus apellidos: ")
usuario["edad"] =input("ingrese su edad: ")
usuario["dni"] = input("Ingrese su DNI: ")

print(usuario.keys())

profesion=input("Ingrese su profesión: ")
usuario["profesion"] = profesion

del usuario["dni"]
print("El diccionario sin edad es :{}".format(usuario.keys()))
print(usuario.values())

