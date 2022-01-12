from modulo_auto import Auto
from modulo_auto_electrico import AutoElectrico

new_beetle = Auto("volkwagen", "new beetle", 2016)
print(new_beetle.obtener_descripcion())

tesla = AutoElectrico("tesla", "roadster", 2016)
print(tesla.obtener_descripcion())