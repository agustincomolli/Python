from mylib import clear_screen, color_me, input_color

web_site = {
    "Nombre": None,
    "URL": None,
    "Descripción": None,
    "Calificación": None
}

clear_screen()

print(color_me("🌟 Calificación del Sitio Web 🌟\n", "yellow"))

for key in web_site.keys():
    web_site[key] = input_color(f"{key}: ", color_input="green")
print()
for key, value in web_site.items():
    print(f"{key}: {value}")