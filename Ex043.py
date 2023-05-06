sexo = int(input('Digite (1) se você for Homem e (2) se você for Mulher: '))
peso = float(input('Digite seu peso: (Kg) '))
alt = float(input('Digite sua altura: (m) '))

imc = peso / (alt * alt)

if sexo == 1:
    print('Você é do sexo masculino e tem um IMC de {:.1f}'.format(imc))
    if imc < 20.7:
        print('Você está abaixo do peso.')
    elif 26.4 > imc > 20.7:
        print('Seu peso é ideal.')
    elif 27.8 > imc > 26.4:
        print('Você está marginalmente acima do peso.')
    elif 31.1 > imc > 27.8:
        print('Você está acima do peso.')
    else:
        print('Você está obeso.')
elif sexo == 2:
    print('Você é do sexo feminino e tem o IMC de {:.1f}'.format(imc))
    if imc < 19.1:
        print('Você está abaixo do peso.')
    elif 25.8 > imc > 19.1:
        print('Seu peso é ideal.')
    elif 27.3 > imc > 25.8:
        print('Você está marginalmente acima do peso.')
    elif 32.3 > imc > 27.3:
        print('Você está acima do peso.')
    else:
        print('Você está obesa.')