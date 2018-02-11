def pasar_segundos(horas,minutos,segundos):
	segundo=(horas*3600)+(minutos*60)+segundos
	return segundo

def calcular_coste(segundos,coste):
	facturacion=coste*segundos
	return facturacion

def convertir_euros(centimos):
	euros=centimos/100
	return euros