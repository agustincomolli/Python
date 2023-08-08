import csv


with open("./archivo.csv", mode="r", encoding="UTF-8") as file:
    # print("Archivo leído correctamente:")
    # print(f"\n{file.read()}\n")

    file_content = csv.reader(file)
    for row in file_content:
        print(row)
