from funcionesboletin8 import pasar_segundos, calcular_coste, convertir_euros

tarifa=int(input("Dime el coste por segundo en centimos: "))
comunicaciones=int(input("Dime el nº de comunicaciones que has realizado: "))
duracioncomunicaciones=[]
segundostotales=0
llamadas=1

for i in range(comunicaciones):
	listallamadas=[]
	comunicacion=input("¿Duracion de la llamada(formato horas/minutos/segundos): ".format(i+1))
	hora=int(comunicacion.split("/")[0])
	minuto=int(comunicacion.split("/")[1])
	segundo=int(comunicacion.split("/")[2])
	listallamadas.append(llamadas)
	listallamadas.append(pasar_segundos(hora,minuto,segundo))
	duracioncomunicaciones.append(listallamadas)
	llamada+=1

for i in duracioncomunicaciones:
	segundostotales+=i[1]

for i in duracioncomunicaciones:
	print("El coste de la llamada {} es {} €".format(i[0],convertir_euros(int(calcular_coste(i[1],tarifa)))))

print("La factura total es de {} €".format(convertir_euros(calcular_coste(segundostotales,tarifa))))