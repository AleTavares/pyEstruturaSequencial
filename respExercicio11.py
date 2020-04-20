# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:*

nInt1 = int(input('Digite o Primeiro Numero Inteiro: '))
nInt2 = int(input('Digite o Segundo Numero Inteiro: '))
nReal1 = float(input('Digite o Primeiro Numero Real: '))

# - o produto do dobro do primeiro com metade do segundo .
resposta = (nInt1 * 2) * (nInt2 / 2)
print('O produto do dobro do primeiro com metade do segundo \n Resposta: {}'.format(resposta))

# - a soma do triplo do primeiro com o terceiro.
resposta = (nInt1 * 3) + nReal1 
print('A soma do triplo do primeiro com o terceiro \n Resposta: {}'.format(resposta))

# - o terceiro elevado ao cubo.
resposta = nReal1**3
print('O terceiro elevado ao cubo \n Resposta: {}'.format(resposta))
