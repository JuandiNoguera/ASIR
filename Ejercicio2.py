'''Realiza un programa que te informe de cuanto vale cada comunicación y el 
total de dinero de todas las comunicaciones. En esta ocasión los datos de la duración 
de las comunicaciones y la tarifa por segundos se encuentran en este fichero donde 
en la primera línea te encuentras la tarifa, y en las restantes la duración de cada 
una de las comunicaciones expresadas en horas, minutos y segundos.'''

from funcionesboletin8 import pasar_segundos, calcular_coste, convertir_euros

with open("comunicaciones.txt", "r") as doc:
	fichero=doc.readlines()

l1=[]
tarifa=0
contador=0
acumulador=0

for elem in fichero:
	l1.append(elem.strip('\n'))

for elem in l1[0]:
	centimo = 0
	if elem.isdigit():
		centimo += int(elem)
	l1[0] = centimo
tarifa = centimo
l1.pop(0)
for elem in l1:
	acumulador+=1
	horas = int(elem.split(':')[0])
	minutos = int(elem.split(':')[1])
	segundos = int(elem.split(':')[2])
	segun=pasar_segundos(horas, minutos, segundos)
	centimos=calcular_coste(segun,tarifa)
	contador+=centimos
	euros=convertir_euros(centimos)
	print("El coste por la llamada {} es {} €.".format(acumulador,euros))

factura=convertir_a_euros(contador)
print("El coste total es de: {} €.".format(factura))