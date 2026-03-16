# Podemos escrever um resultado na quantidade de caracteres especifica ao colocar o valor dentro da máscara apos escrever

nome = input ('Qual é o seu nome?')
print('Prazer em conhece-lo {:20}!'.format(nome))

#Alinhamento de máscara
#Podemos alinhas o nome dentro do número de caracteres que desejamos

#Alinhamento para direita
nome = input ('Qual é o seu nome?')
print('Prazer em conhece-lo {:>20}!'.format(nome))

#Alinhamento para a esquerda 
nome = input ('Qual é o seu nome?')
print('Prazer em conhece-lo {:<20}!'.format(nome))

#Alinhamento no centro 
nome = input ('Qual é o seu nome?')
print('Prazer em conhece-lo {:^20}!'.format(nome))
