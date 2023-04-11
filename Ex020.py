import random
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
lista = [a,b,c,d]
random.shuffle(lista)
print('A ordem dos alunos é: ')
print(lista)
