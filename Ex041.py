from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
idade = atual - ano
print('Sua idade é \033[1:36m{}\033[m.'.format(idade))
if 9 >= idade > 0:
    print('Sua categoria é a \033[1:31mMIRIM\033[m.')
elif 14 > idade > 9:
    print('Sua categoria é \033[1:32mINFANTIL\033[m.')
elif 19 >= idade > 14:
    print('Sua categoria é \033[1:33mJUNIOR\033[m.')
elif 25 >= idade > 19:
    print('Sua categoria é \033[1:34mSENIOR\033[m.')
elif idade > 25:
    print('Sua categoria é \033[1:36mMASTER\033[m')
elif idade < 0:
    print('Você é um viajante do futuro?')
