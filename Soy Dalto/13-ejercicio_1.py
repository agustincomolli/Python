# Este curso = 1.5 horas
# Curso mínimo = 2.5 horas
# Curso promedio = 4 horas
# Curso máximo = 7 horas
# Videos en crudo de este curso = 3.5 horas
# Videos en crudo de un curso promedio = 5 horas

# a) Diferencia en porcentaje entre el curso actual y:
#   1 - el más rápido de los otros cursos
#   2 - el más lento de los otros cursos
#   3 - el promedio de los otros cursos

# b) Porcentaje de material inservible que se reduce en:
#   1 - el promedio de los otros cursos
#   2 - este curso

# c) ¿Ver 10 horas de este curso a cuántas de otros equivale?
#    ¿Y al revés?

# Duración de los cursos
this_course = 1.5 # Curso actual
min_course = 2.5  # Curso más rápido
mean_course = 4   # Curso promedio
max_course = 7    # Curso más lento

# Duración de los videos en crudo
raw_this_course = 3.5
raw_mean_course = 5

# a - 1) Diferencia en porcentaje entre el curso actual y el más rápido
average_this_course = (this_course * 100) / min_course
difference = 100 - average_this_course
difference = round(difference, 2)
print(f"La diferencia con el curso más rápido es de {difference} %")
# a - 2) Diferencia en porcentaje entre el curso actual y el más lento
average_this_course = (this_course * 100) / max_course
difference = 100 - average_this_course
difference = round(difference, 2)
print(f"La diferencia con el curso más lento es de {difference} %")
# a - 3) Diferencia en porcentaje entre el curso actual y el promedio
average_this_course = (this_course * 100) / mean_course
difference = 100 - average_this_course
difference = round(difference, 2)
print(f"La diferencia con el curso promedio es de {difference} %")

# b - 1) Porcentaje de material inservible que se reduce en comparación con el 
# promedio de los otros cursos
average_mean_course = (mean_course * 100) / raw_mean_course
difference = 100 - average_mean_course
difference = round(difference, 2)
print(f"\nLos cursos promedio tiene un {difference} % de material inservible")
# b - 2) Porcentaje de material inservible que se reduce en comparación con el 
# curso actual
average_this_course = (this_course * 100) / raw_this_course
difference = 100 - average_this_course
difference = round(difference, 2)
print(f"Este curso tiene un {difference} % de material inservible")

# c - 1.1) 10 horas de este curso son X horas del curso más rápido.
one_hour = min_course / this_course
equivalence = 10 * one_hour
equivalence = round(equivalence, 2)
message = "\n10 horas de este curso equivalen a "
message += f"{equivalence} horas del curso más rápido"
print(message)
# c - 1.2) 10 horas de este curso son X horas del curso promedio.
one_hour = mean_course / this_course
equivalence = 10 * one_hour
equivalence = round(equivalence, 2)
message = "10 horas de este curso equivalen a "
message += f"{equivalence} horas del curso promedio"
print(message)
# c - 1.3) 10 horas de este curso son X horas del curso más lento.
one_hour = max_course / this_course
equivalence = 10 * one_hour
equivalence = round(equivalence, 2)
message = "10 horas de este curso equivalen a "
message += f"{equivalence} horas del curso más lento"
print(message)

# c - 2.1) 10 horas del curso más rapido son X horas de este curso.
equivalence = (10 * this_course) / min_course
equivalence = round(equivalence, 2)
message = "\n10 horas del curso más rápido equivalen a "
message += f"{equivalence} horas de este curso"
print(message)
# c - 2.2) 10 horas del curso promedio son X horas de este curso.
equivalence = (10 * this_course) / mean_course
equivalence = round(equivalence, 2)
message = "10 horas del curso promedio equivalen a "
message += f"{equivalence} horas de este curso"
print(message)
# c - 2.3) 10 horas del curso más lento son X horas de este curso.
equivalence = (10 * this_course) / max_course
equivalence = round(equivalence, 2)
message = "10 horas del curso más lento equivalen a "
message += f"{equivalence} horas de este curso"
print(message)
