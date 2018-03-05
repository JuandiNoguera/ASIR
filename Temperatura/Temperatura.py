'''Realiza un programa que te pida el nombre de un municipio de la 
provincia de Sevilla, y si existe te muestre la 
temperatura máxima y mínima actuales.'''

from lxml import etree

doc=etree.parse("sevilla.xml")
cps=doc.findall("municipio")
l1=[]
l2=[]

for cp in cps:
	valor=str(cp.attrib["value"])
	ids=valor.split("-id")
	l1.append(ids[0])
	l2.append(ids[1])

municipios=input("Introduce el nombre del municipio: ")
cadena=municipios.lower().replace(" ","-")

for x,y in zip(l1,l2):
	if cadena==x:
		codigo=y
		url=etree.parse("http://www.aemet.es/xml/municipios/localidad_"+codigo+".xml")

		maxima=url.find("prediccion/dia/temperatura/maxima")
		minima=url.find("prediccion/dia/temperatura/minima")

print("Las maxima son",maxima.text)
print("Las minima son",minima.text)