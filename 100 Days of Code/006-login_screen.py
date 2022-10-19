print("\033[33mInicio de Sesión:")
print("+" * 17)
print()

username = input("Usuario: \033[32m")
password = input("\033[33mContraseña: \033[32m")
message = """
Hola, {user}, qué acento tan encantador tienes, podrías haber entrado aquí con encanto incluso sin una contraseña.

Qué tengas un lindo día.

¡No olvides usar un sombrero al sol!
"""

print("\033[33m", end="")

if username == "agustincomolli" and password == "admin":
  print(message.replace("{user}", "Agustín"))
elif username == "lormelmir" and password == "milk & mocha":
  print(message.replace("{user}", "Lorena"))
elif username == "usuario" and password == "invitado":
    print("Hola invitado, bienvenido.\n\nQue tengas un lindo día.")
else:
  print("¡Vete a tomar por culo! 🤌🏼")
  print("\033[0m")