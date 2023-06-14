nome = str(input('Digite se nome: ')).strip().title()
while (len(nome)) <= 3:
    print('O nome tem que contér mais de 3 caracteres')
    nome = str(input('Digite se nome: ')).strip().title()
idade = int(input('Digite sua idade: '))
while (idade < 0) or (idade > 130):
    if idade < 0:
        print('Digita a idade certa, "De Volta Para o Futuro"...')
        idade = int(input('Digite sua idade: '))
    elif idade > 130:
        print('Deixa de frescura que tu não é uma múmia...')
        idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: '))
while salario <= 0:
    print('Tá pagando para trabalhar é? Trabalha pra mim então, corno!')
    salario = float(input('Digite seu salário: '))
sexo = str(input('''Digite seu sexo: 
 [M] - Masculino
 [F] - Feminino
[NB] - Não binário
[NI] - Não quero informar
Digite uma opção: ''')).strip().upper()
while (len(sexo)) > 2 and sexo not in 'MFNBI':
    print('Opção Inválida')
    sexo = str(input('''Digite seu sexo: 
     [M] - Masculino
     [F] - Feminino
    [NB] - Não binário
    [NI] - Não quero informar
    Digite uma opção: ''')).strip().upper()
estciv = str(input('''Digite seu estado civíl:
[S] - Solteiro(a)
[C] - Casado(a)
[V] - Viuvo(a)
[D] - Divorciado(a)
Digite uma opção:''')).strip().upper()
while (len(estciv) < 1) or (len(estciv) >1) and estciv not in 'SCVD':
    print('Opção inválida')
    estciv = str(input('''Digite seu estado civíl:
    [S] - Solteiro(a)
    [C] - Casado(a)
    [V] - Viuvo(a)
    [D] - Divorciado(a)
    Digite uma opção:''')).strip().upper()
print('--' * 20)
print(f'''Nome = {nome}.
Idade = {idade}
Salário = {salario:.2f}
Sexo = {sexo}
Estado Civíl = {estciv}''')