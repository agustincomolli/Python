# IF, ELSE
age = 46

# Si la operación de comparación es True, entonces...
if age >= 18: # ---> operación de comparación
    # Ejecutar este bloque de código.
    print("¡Sos mayor de edad! 👨")
# Si la operación de comparación es False, entinces...
else:
    # Ejecutar este otro bloque de código.
    print("Sos menor de edad 👶")


user_password = "MyP4ssW0rd"
saved_password = "MyN3wP4ssW0rd"

if user_password == saved_password:
    print("\nIniciando sessión...")
else:
    print("\nContraseña inválidad. Intente nuevamente...")

# IF, ELIF, ELSE...
salary = 1000
print(f"\nTienes un salario de u$s {salary}")

if salary > 10000:
    print("Estás bien enconómicamente en cualquier lado")
elif salary > 1000:
    print("Estás bien económicamente en Argentina")
else:
    print("Sos pobre")

# IF anidados.

monthly_income = 1500 # Ingreso mensual
monthly_expense = 1000 # Gasto mensual
print("\nInforme de gastos mensuales")

if monthly_income > 1000:
    if (monthly_income - monthly_expense) < 0:
        print("Estás en rojo 🟥")
    elif (monthly_income - monthly_expense) > 250:
        print("Estás bien 👌")
    else:
        print("Estás gastando mucho, ten cuidado 🤑")