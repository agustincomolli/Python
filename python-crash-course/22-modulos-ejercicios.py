import modulo_ejercicio
from modulo_ejercicio import mostrar_diseños_completados

diseños_a_imprimir = ["carcasa iphone", "robot", "dodecaedro"]
diseños_completados = []
print("\nDiseños 3D")
modulo_ejercicio.imprimir_modelos(diseños_a_imprimir, diseños_completados)
mostrar_diseños_completados(diseños_completados)