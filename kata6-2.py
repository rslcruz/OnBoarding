# Lista de planetas
planetas = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

# Solicitamos el nombre de un planeta *Pista:  input()*
planeta_input = input('Ingrese el nombre del planeta')
# Busca el planeta en la lista

planeta_indice = planetas.index(planeta_input)
# Muestra los planetas más cercanos al sol

print('Estos son las planetas mas cercanos que ' + planeta_input)
print(planetas[0:planeta_indice])
# Muestra los planetas más lejanos al sol

print('Estos son los planetas mas lejanos que ' + planeta_input)
print(planetas[planeta_indice + 1:])