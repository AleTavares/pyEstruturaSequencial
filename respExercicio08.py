# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
vlrHora = float(input('Digite o Valor cobrado por hora: '))
qtdHoras = float(input('Digite a quantidade de horas trabalhadas: '))
vlrTotal = vlrHora * qtdHoras
print('Seu salario será de: R$ {}'.format(vlrTotal))