# Almacenar las entradas del usuario
planeta1 = input('Introduzca la distancia del sol para el primer planeta en KM')
planeta2 = input('Introduzca la distancia desde el sol para el segundo planeta en KM')


# Convierte las cadenas de ambos planetas a números enteros
planeta1 = int(planeta1)
planeta2 = int(planeta2)


# Realizar el cálculo y determinar el valor absoluto
distancia_km = planeta1 - planeta2
print(distancia_km)

# Convertir de KM a Millas
distancia_mi = distancia_km * 0.621
print(abs(distancia_mi))