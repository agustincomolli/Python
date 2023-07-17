"""
Pedir al usuario que diga frase y:
1) Calcular cuánto tardaría en decir esa frase si en un segundo dice 2 
   palabras.
2) ¿Cuántas palabras dijo?
3) Si tarda más de 1 minuto decirle:
   "Pará flaco tampoco te pedí un testamento."
4) Dalto habla un 30% más rápido. ¿Cuánto tardaría él en decir la frase?

"""
phrase = input("Escribe el texto que leerás en voz alta: ")
words = phrase.split()
speak_time = len(words) // 2
print(f"1) Has dicho la frase en {speak_time} segundos.")
print(f"2) Has dicho {len(words)} palabras")
if speak_time > 60:
    print("3) Pará flaco tampoco te pedí un testamento.")
dalto_speak_time = speak_time - (0.3 * speak_time)
print(f"4) Dalto lo diría en {dalto_speak_time} segundos")