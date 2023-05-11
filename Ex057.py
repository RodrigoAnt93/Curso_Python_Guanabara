sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
        sexo = str(input('Você não digitou uma opção válida. Qual o seu sexo [M/F]: ')).upper().strip()
print('O sexo que você digitou foi {}'.format(sexo))
