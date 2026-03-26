import math
num1 = float(input("Digite um número "))
raiz = math.sqrt(num1)
print('a raiz de {} é igual a {}'.format(num1, math.ceil(raiz))) #ceil arredonda pra cima
print('a raiz de {} é igual a {}'.format(num1, math.floor(raiz))) #floor arredonda pra baixo

from math import sqrt, floor, ceil
num = int(input('Digite um número: ' ))
raiz = sqrt(num)
print('a raiz de {} é igual a {}'.format(num, ceil(raiz))) # arredonda pra cima
print('a raiz de {} é igual a {}'.format(num, floor(raiz))) # arredonda para baixo
