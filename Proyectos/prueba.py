import mylib
from mylib import Colors, TextStyles, highlight_text, align_text
print(align_text(highlight_text("Bienvenido a Python", Colors.BLUE,TextStyles.UNDERLINE), "center"))