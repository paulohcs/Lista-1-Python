#!/usr/bin/python3

km = float(input('Km percorridos: '))
dias = int(input('Dias: '))

print('Preco a pagar: R$ ' + str(float(dias*60 + km*0.15)))
