'''Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
finalizar.'''

multiples_of_5=[]
non_multiples_of_5=[]

number=int(input('Enter a number: '))

for i in range(1,number+1):
    if (i%5==0):
        multiples_of_5.append(i)
    else:
        non_multiples_of_5.append(i)

print(f'Multiples of 5: {multiples_of_5}')
print(f'Non multiples of 5: {non_multiples_of_5}')