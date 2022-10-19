is_fan = False
print("\033[33m", end="") # cambia el color a amarillo.

print("🔎 Detector de falso fan de Robotech 👀\n", "*" * 26, "\n")

season = int(input("¿Cuál es la temporada que más te gustó? \033[32m"))

if season == 1:
  print("\033[33mSin dudas es la mejor.")
  ship_type = input("¿Cómo se llaman las naves de combate que usaba el protagonista? \033[32m")
  if ship_type == "Varitech":
    print("\033[33m¡Bien!")
    enemy_name = input("¿Dime el nombre de uno de los enemigos? \033[32m")
    if enemy_name == "Britai" or enemy_name == "Kairon" or enemy_name == "Miriya" or \
      enemy_name == "Asonya" or eneny_name == "Exedoor":
      is_fan = True
    else:
      print("\033[33mEse nombre no existe.")
elif season == 2:
  print("\033[33mEs la peor temporada que hay.")
  lover_boy = input("¿Cómo se llamaba el chico del que se enamora la protagonista? \033[32m")
  if lover_boy == "Zor Prime":
    print("\033[33m¡Exelente!")
    is_fan = True
elif season == 3:
  print("\033[33mEsta temporada me gustó muchísimo.")
  aliens = input("¿Cómo se llamaban los aliens que invadieron el planeta? \033[32m")
  if aliens == "Invid":
    print("\033[33m¡Exacto!")
    is_fan = True
else:
  print("\033[33mLa cagaste")
  print("¡No hay más que 3 temporadas!")

if is_fan:
  print("\033[33m¡Conocés bien la serie. Felicitaciones! 🤩")
else:
  print("\033[33mEres un falso fan, vete a tomar por culo. 😡")
  
print("\033[33m")  # restable el color por defecto.