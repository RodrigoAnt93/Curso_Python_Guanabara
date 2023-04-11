nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome completo em maiusculo fica: {}'.format(nome.upper()))
print('Seu nome completo em minusculo fica: {}'.format(nome.lower()))
print('Seu nome tem {} letras!'.format(len(nome) - nome.count(' ')))
sep = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(sep[0], len(sep[0])))

