# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:*
vlrHora = float(input('Quanto você ganha por hora: '))
horasTrabalhadas = float(input('Quantas horas trabalhou esse mês: '))

# - salário bruto.
salarioBruto = vlrHora * horasTrabalhadas

# - quanto pagou ao INSS.
valorInss = salarioBruto * 0.08

# - quanto pagou ao sindicato.
valorSindicato = salarioBruto * 0.05

# - o salário líquido.
valorIR = salarioBruto * 0.11
salarioLiquido = salarioBruto - (valorInss + valorSindicato + valorIR)
# - calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   - Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$
print('- Salário Bruto : R$ {}'.format(salarioBruto))
print('- IR (11%) : R$ {}'.format(valorIR))
print('- INSS (8%) : R$ {}'.format(valorInss))
print('- Sindicato ( 5%) : R$ {}'.format(valorSindicato))
print('= Salário Liquido : R$ {}'.format(salarioLiquido))
#   *Obs.: Salário Bruto - Descontos = Salário Líquido.*

