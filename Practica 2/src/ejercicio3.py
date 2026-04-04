# Práctica 2, ejercicio 3

def filter_spoilers(review):
    list_of_spoiler_words = input("Enter a list of words you consider spoilers: ")
    list_of_spoiler_words = list_of_spoiler_words.split(",")
    for word in list_of_spoiler_words:
        word = word.strip()
        review = review.replace(word.lower(), len(word) * '*')
        review = review.replace(word.upper(), len(word) * '*')
        review = review.replace(word.capitalize(), len(word) * '*')
    
    print(review)

review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""