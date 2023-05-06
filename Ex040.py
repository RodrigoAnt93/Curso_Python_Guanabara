n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
med = (n1 + n2) / 2
print('A média da suas notas são \033[1:36m{}\033[m'.format(med))
if med < 5.0:
    print('Infelizmene você foi \033[1:31mREPROVADO\033[m.')
elif med == 5.0 or med < 7.0:
    print('Sua média não foi o ideal e você está em \033[1:33mRECUPERAÇÃO\033[m.')
elif med > 6.9:
    print('Você foi \033[1:32mAPROVADO\033[m. Parabéns')