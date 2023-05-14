numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Desessis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
opc = int(input('Digite um número para ele se escrito por extenso: '))
while opc < 0 or opc > 20:
    opc = int(input('Tente novamente. Digite um número para ele se escrito por extenso: '))