import xml.etree.ElementTree as ET

datos = '''
<persona>
    <nombre>Agustín</nombre>
    <telefono type="intl">
        2226 680056
    </telefono>
    <correo hide="yes" />
</persona>
'''
arbol = ET.fromstring(datos)
print("Nombre:", arbol.find("nombre").text)
print("Atributos:", arbol.find("correo").get("hide"))