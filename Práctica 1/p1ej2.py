'''Escribe un programa que solicite al usuario una cantidad de segundos y muestre
cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
hora, 1 minuto y 1 segundo.'''

user_seconds = int(input('Enter an amount of seconds: '))
hours = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = user_seconds % 60



print(f'{user_seconds} seconds are {hours} hour/s, {minutes} minute/s and {seconds} second/s.')
