from mylib import clear_screen, color_me, input_color


def is_palindrome(word: str):
    """
        DESCRIPTION: Devuelve True si la palabra es un palíndromo.
        PARAMETERS: 
                    word: Palabra a verificar.

    """

    if len(word) <= 1:
        return True

    if word[0] == word[-1]:
        word = word[1:-1]
        return is_palindrome(word)
    else:
        return False


clear_screen()
print(color_me("🙂 Verificador de Palíndromos 🙃\n", "yellow"))
word = input_color("Ingrese una palabra: ", color_input="green")

if is_palindrome(word.lower()):
    print("\nLa palabra " + color_me("ES", "yellow") + " palíndromo.")
else:
    print("\nLa palabra " + color_me("NO", "red") + " es palíndromo.")
