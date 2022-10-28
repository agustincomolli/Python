def login():
    import getpass

    while True:
        user = input("Usuario: ")
        password = getpass.getpass("Contraseña: ")

        if user == "agustincomolli" and password == "C0ntr4señ@":
            print("\nBienvenido Agustín Comolli")
            break
        else:
            print("Usuario o contraseña inválida. Intente otra vez.\n")

print("Inicio de sesión\n")

login()
