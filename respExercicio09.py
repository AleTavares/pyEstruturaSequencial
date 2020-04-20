# 9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).
temperatura = float(input('Digite a temperatura em Farenheit: '))
celsius = (5 * (temperatura - 32) / 9)
print('{} Farenheit convertido em Celsius é {}'.format(temperatura, celsius))