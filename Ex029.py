from time import sleep
vel = int(input('Qual foi a velocidade que você passou no radar? '))
if vel <= 80:
    sleep(2)
    print('Você estava dentro da velocidade permitida')
else:
    mul = (vel - 80) * 7
    sleep(3)
    print('Você estava acima da velocidade. Você será multado e sua multa será de R${}'.format(mul.__float__()))

