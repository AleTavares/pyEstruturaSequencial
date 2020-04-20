# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
# formula: (°C × 9/5) + 32 =  °F
temperatura = float(input('Digite a temperatura em Celsius: '))
farenheit = (temperatura * 9 / 5) +32
print('{} Celsius convertido em Farenheit é {}'.format(temperatura, farenheit))