'''Escribe un programa que simule una caja registradora: el usuario ingresa precios de
productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
acumulado. Nota: utilizá la sentencia break cuando haga falta.'''

price = float(input('Enter product price: '))
total = 0
while price != 0:
    total = total + price
    price = float(input('Enter product price: '))

print(f'Total: {total}')