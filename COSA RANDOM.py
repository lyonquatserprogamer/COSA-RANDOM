palabras_absurdas_de_uru_dict = {
    'ALVR:un insulto que se usa mucho en uruguay y argentina'
    'CULERO: significa que alguien es molesto'
    'PA: significa en uruguayo no saves'
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in palabras_absurdas_de_uru_dict.keys():
    print(palabras_absurdas_de_uru_dict[word])
else:
    print('esa palabra no esta en el diccionario')
