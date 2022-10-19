print("\033[33m", end="")
print("*** Generador de insultos 👿 ***\n")

name = input("Tu nombre: \033[32m")
print("\033[33m", end="")
day = input("¿Qué día es hoy? \033[32m")

if day == "lunes":
  message = "no iré a tu funeral, pero enviaré una bonita carta aprobándolo."
elif day == "martes":
  message = "¿por qué no vas a ver si está lloviendo en la esquina?"
elif day == "miércoles" or day == "miercoles":
  message = "que tengas un buen día… en cualquier otro lugar."
elif day == "jueves":
  message = "sé lo que la gente dice de ti… tienen razón."
elif day == "viernes":
  message = "eres tan brillante como un agujero negro y el doble de denso."
elif day == "sábado" or day == "sabado":
  message = "espero que el resto de tu día sea tan agradable como tú."
elif day == "domingo":
  message = "deberías tratar de comer un poco de maquillaje para ser una persona más bella por dentro."
else:
  message = "Ya la cagaste con el día."

name = name.capitalize()

print(f"\n\033[1,32m{name}\033[33m, {message} 🤣\033[0m")