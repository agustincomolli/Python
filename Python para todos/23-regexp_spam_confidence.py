import re

try:
    archivo = open("mbox-short.txt", mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

spam_confidence = []
patron_regexp = "^X-DSPAM-Confidence: ([0-9.]+)"
lista = []

for linea in archivo:
    linea = linea.rstrip()
    spam_confidence = re.findall(patron_regexp, linea)
    if len(spam_confidence) != 1: continue
    numero_spam = float(spam_confidence[0])
    lista.append(numero_spam)

print("El máximo número de spam confidence es:", max(lista))
archivo.close()