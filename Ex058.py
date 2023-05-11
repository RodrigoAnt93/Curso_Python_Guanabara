import random
from random import randint
from time import sleep
print('~~' * 40)
print('Acabei de pensar em um número entre 0 e 10...')
print('~~' * 40)
play = int(input('Você consegue adivinhar o número? '))
c = 0
cpu = randint(0, 10)
while cpu != play:
    c += 1
    print('Óbvio que você errou!')
    play = int(input('Vou deixar você tentar outra vez: '))

print('Nossa você acertou!! Você precisou de {} chances para acertar...'.format(c))

