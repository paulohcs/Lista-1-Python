#!/usr/bin/python3

salario = float(input('Salário: '))
aumento = float(input('% de Aumento: '))

print('Aumento de ' + str((aumento/100) * salario) + ' R$')
print('Novo salário: R$ ' + str(float(salario + ((aumento/100) * salario))))
