from datetime import date
cadastro = {}
while True:
    cadastro["nome"] = str(input('Nome: ')).strip().capitalize()
    cadastro["idade"] = date.today().year - int(input('Ano: '))
    cadastro["CTPS"] = int(input('Carteira de trabalho (0 se não tiver): '))
    if cadastro["CTPS"] == 0:
        del cadastro["CTPS"]
        break
    cadastro["ano_contratacao"] = int(input('Ano de contratação: '))
    cadastro["salario"] = float(input('Salário: R$'))
    cadastro["aposentadoria"] = cadastro["idade"] + ((cadastro["ano_contratacao"] + 35) - date.today().year)
    break
print('-=' * 20)
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')
