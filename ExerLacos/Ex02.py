login = str(input('Digite seu login: ')).strip()
senha = str(input('Digite sua senha: ')).strip()
while login == senha:
    print('A senha tem que ser diferente do login, animal...')
    login = str(input('Digite seu login: ')).strip()
    senha = str(input('Digite sua senha: ')).strip()
print('Conta criada com sucesso!')