# Crea un diccionario llamado planet con los datos propuestos

planet = {
    'name': 'Mars',
    'moons': 2
}

# Muestra el nombre del planeta y el número de lunas que tiene.

print(f'{planet["name"]} has {planet["moons"]} moons')
# Agrega la clave circunferencia con los datos proporcionados previamente

planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

# Imprime el nombre del planeta con su circunferencia polar.
print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')


# --------------------  Ejercicio #2  ------------------------------------------


# Añade el código para determinar el número de lunas.

# Obtenemos la lista de las lunas
# Almacenamos los resultados en una variable moons
moons = planet_moons.values()

# Obtenemos el total de planetas
# Almacenamos los resultados en una variable llamada years
planets = len(planet_moons.keys())
# Calcula el total_moons agregando todas las lunas
# Almacena su valor en una variable llamada total_moons



total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

# Calcula el promedio dividiendo el total_moons por el número de planetas
average = total_moons / planets

# Muestra el promedio
print(average)