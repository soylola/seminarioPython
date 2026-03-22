'''Escriba en un archivo llamado questions.py el siguiente programa en Python.'''

import random

# dic = clave:valor

words = { "Programación": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista",],
        "Nombres": ["lola", "sofía", "agustina", "ana", "ludmila", "bianca", "patricia", "claudia"],
        "Animales":  ["serpiente", "koala", "carpincho", "perezoso", "aguila", "hormiga"]
        }


guessed = []
attempts = 6
points = 0
print("¡Bienvenido al Ahorcado!")
print ("Categorías disponibles: ")
for category in words.keys():
    print(f"• {category}")

chosen_category = input("Elegí una categoría: ")

if chosen_category in words.keys():
    print(f"Elegiste la categoría: '{chosen_category}'")
    # busca en el diccionario words el valor de la clave "chosen_category" y lo guarda en la variable word_list
    word_list = words[chosen_category]
    word = random.choice(word_list)
    print()

    while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            points += 6
            print("¡Ganaste!")
            print(f"Puntos actuales: {points}")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        print(f"Puntos: {points}")

        letter = input("Ingresá una letra: ")
        if len(letter)==1:
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                points -= 1
                print("Esa letra no está en la palabra.")
            print()
        else:
            print('Entrada no válida.')
    else:
        points = 0
        print(f"¡Perdiste! La palabra era: {word}")
else:
    print("La categoría elegida no existe.")