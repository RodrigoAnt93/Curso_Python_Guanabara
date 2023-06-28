from datetime import date
contratacao = int(input('Digite o ano que você foi contratado: '))
salario = float(input('Digite seu salário: R$'))
ano = date.today().year - contratacao
pocentagem_aumento = 1.5
salario_atual = salario
valor_aumento = (salario_atual * pocentagem_aumento) / 100
for c in range(1, ano + 1):
    salario_atual += valor_aumento
    pocentagem_aumento *= 2
print('')
print(pocentagem_aumento)
print(valor_aumento)
print((salario_atual * pocentagem_aumento / 100))
print(f'Já se passaram {ano} anos desde que você entrou na empresa. Seu salário começou com R${salario:.2f} e atualmente é R${salario_atual:.2f}')

