#Primero, divide el texto en cada oración para trabajar con su contenido:
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth's """
text.split('. ')
#Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.
# Define las palabras pista: average, temperature y distance suenan bien
palabras = ["average", "temperature", "distance"]
#Cre un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:

# Ciclo for para recorrer la cadena
for sentence in text:
    for key_word in palabras:
        if key_word in sentence:
            print(sentence)
            break

# Ciclo para cambiar C a Celsius
for sentence in text:
    for key_word in palabras:
        if key_word in sentence:
            print(sentence.replace(' C', ' Celsius'))
            break