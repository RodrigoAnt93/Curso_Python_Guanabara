frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A apareceu {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece primeiro em: {}'.format(frase.find('A')+1))
print('A letra A aparece por ultimo em: {}'.format(frase.rfind('A')+1))



