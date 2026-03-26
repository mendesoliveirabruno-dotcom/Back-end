import math
num1 = float(input("Digite um número "))
raiz = math.sqrt(num1)
print('a raiz de {} é igual a {}'.format(num1, math.ceil(raiz))) #ceil arredonda pra cima
print('a raiz de {} é igual a {}'.format(num1, math.floor(raiz))) #floor arredonda pra baixo
