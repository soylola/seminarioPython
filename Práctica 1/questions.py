'''Escriba en un archivo llamado questions.py el siguiente programa en Python.'''

import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
    ]
word = random.choice(words)
guessed = []
attempts = 6
points = 0
print("¡Bienvenido al Ahorcado!")
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