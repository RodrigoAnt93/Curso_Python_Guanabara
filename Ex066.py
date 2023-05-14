cond = ''
soma = 0
cont = 0
maior = 0
menor = 0
while cond != 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    cond = str(input('Você que continuar (S/N)? ')).strip().upper()
print('Você digitou {} números e a média deles é {:.2f}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))