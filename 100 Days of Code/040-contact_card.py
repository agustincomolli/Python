from mylib import color_me, clear_screen, input_color


def fill_contact_card():
    name = input_color("🧑 Nombre: ", color_input="green")
    birthday = input_color("📆 F. de nacimento: ", color_input="green")
    telephone = input_color("☎️ Teléfono: ", color_input="green")
    email = input_color("📧 Email: ", color_input="green")
    address = input_color("🏠 Dirección: ", color_input="green")

    card = {
        "name": name,
        "birthday": birthday,
        "telephone": telephone,
        "email": email,
        "address": address}

    return card

clear_screen()

print(color_me("Tarjeta de contacto 📇\n", "yellow"))

contact_card = fill_contact_card()

print(color_me("\n" + "-" * 30 + "\n", "yellow"))

print(f"Hola {contact_card['name']}.")
print(f"Nuestro diccionario dice que naciste el {contact_card['birthday']},")
print(f"que te podemos llamar al {contact_card['telephone']}, enviar un correo a ")
print(f"{contact_card['email']} o escribirte a ")
print(f"{contact_card['address']}.")