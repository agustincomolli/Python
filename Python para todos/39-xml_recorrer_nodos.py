import xml.etree.ElementTree as ElementTree

datos = '''
    <cosas>
        <usuarios>
            <usuario x="2">
                <id>001</id>
                <nombre>Agustín</nombre>
            </usuario>
            <usuario x="7">
                <id>002</id>
                <nombre>Lorena</nombre>
            </usuario>
        </usuarios>
    </cosas>
'''
arbol = ElementTree.fromstring(datos)
# Excluir de la búsqueda solamente el elemento raíz.
lista_datos = arbol.findall("usuarios/usuario")

print("\nCantidad de usuarios:", len(lista_datos), "\n")

for elemento in lista_datos:
    print("ID:", elemento.find("id").text)
    print("Nombre:", elemento.find("nombre").text)
    print("Atributo:", elemento.get("x"), "\n")
