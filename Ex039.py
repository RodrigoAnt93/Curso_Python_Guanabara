from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
atual = date.today().year
idade = atual - ano
if idade == 0 and idade < 18:
    print('Sua idade é \033[1:32m{}\033[m e faltam \033[1:34m{}\033[m anos para você se apresentar.'.format(idade, 18 - idade))
elif idade == 18:
    print('Sua idade é \033[1:32m{}\033[m e esse ano você tem que ir se apresentar.'.format(idade))
elif idade > 18:
    print('Sua idade é \033[1:32m{}\033[m e a \033[1:31m{}\033[m anos você deveria ter se apresentado. Vá na junta militar para se regularizar.'.format(idade, idade - 18))
elif idade < 0:
    print('\033[7:40mVocê é um viajante do tempo??\033[m')