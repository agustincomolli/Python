print("*** Calculadora de Préstamos ***\n")
print("Préstamo de $1.000 a 10 años al 5% de interés\n")

loan = 1000
debt = loan
apr = 5

for i in range(10):
    debt = round(debt * 1.05, 2)
    print(f"El {i+1}º año es {debt}")

interests = round(debt - loan, 2)
print(f"\nDeberás pagar $ {interests} en intereses.")