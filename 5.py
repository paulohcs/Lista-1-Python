#!/usr/bin/python3

preco = float(input('Preço: '))
desconto = float(input('% de desconto: '))

print('Desconto de R$ ' + str(float((desconto/100) * preco)))
print('Preço a pagar: R$ ' + str(float(preco - ((desconto/100) * preco))))
