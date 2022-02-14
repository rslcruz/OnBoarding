
planeta = ''
planetas = []
# Escribe el ciclo while solicitado

while planeta.lower() != 'done':
    if planeta:
        planetas.append(planeta)
    planeta = input('Ingrese un nuevo planeta')

# Escribe tu ciclo for para iterar en una lista de planetas

for planet in planetas:
    print(planet)