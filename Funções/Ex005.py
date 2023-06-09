def TaxaImposto(val, taval):
    valor = val
    taxa_imposto = taval
    print(f'O valor do produto é {float(valor)} e com o imposto fica por {(valor * taxa_imposto / 100) + valor:.2f}')


valor = float(input('Digite o valor da compra: R$'))
taxa = int(input('Digite a pocentagem aplicada na compra: '))
TaxaImposto(valor, taxa)