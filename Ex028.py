import random
from time import sleep
print('~' * 100)
print('Acabei de pensar em um número entre 0 e 5...')
print('~' * 100)
num = int(input('Você consegue adivinhar o número? '))
cpu = random.randint(0, 5)
print('Processando... Hum...')
sleep(3)
if cpu == num:
    print('Cara, você acertou...Você é adivinha??')
else:
    print("Óbvio que você errou!! Eu pensei em {} e você falou {}.".format(cpu, num))
