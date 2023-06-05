def calc_eleitor(a):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - a
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO FACULTATIVO'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


ano_nasci = int(input('Digite seu ano de nacimento: '))
print(calc_eleitor(ano_nasci))