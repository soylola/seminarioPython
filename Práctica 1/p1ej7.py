'''Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
espacios. Las palabras cortas deben ser excluidas del resultado final.'''

list_of_words = input('Enter a list of words separated by spaces: ').split()

long_words = []

for word in list_of_words:
    if len(word)>3:
        long_words.append(word)

sentence = " ".join(long_words)
print(sentence)