#!/usr/bin/python3

cigarros = int(input('Cigarros fumados por dia: ' ))
anos = int(input('Anos que fumou: '))

qntCigarros = anos*365*cigarros

dias = int((qntCigarros*10)/1440)

print('Redução do tempo de vida em ' + str(dias) + ' dias')


