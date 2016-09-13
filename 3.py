#!/usr/bin/python3

dias = int(input('Dias : '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

total = dias*24*60*60

total += horas*60*60

total += minutos*60

total += segundos

print(str(dias) + ' dias, ' + str(horas) + ' horas, ' + str(minutos) + ' minutos e ' + str(segundos) + ' segundos')
print('Total: ' + str(total) + ' segundos')
