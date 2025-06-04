from random import choice

print('=' * 20)
resp = input('Advinhe o número entre 0 e 5:')
num =['0','1','2','3','4','5']
escolha = choice(num)

if resp == escolha:
    print('Parabéns!!! Você acertou o número que eu pensei')
else:
    print('Que pena. o número que eu pensei era o {}' .format(escolha))