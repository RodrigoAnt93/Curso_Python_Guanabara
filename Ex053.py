frase = str(input('Digite a frase: ')).strip().upper()
div = frase.split()
junta = ''.join(div)
inverte = ''
for letra in range(len(junta) -1, -1, -1):
    inverte += junta[letra]
if inverte == junta:
    print('Sua frase é um palindromo')
else:
    print('Sua frase não é um palindromo')