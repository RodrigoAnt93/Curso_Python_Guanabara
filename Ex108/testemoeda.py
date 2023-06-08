from Ex112 import moeda
from Ex112 import dados

valor = dados.leiamoeda("Digite o valor: ")
taxa_mais = int(input('Digite a taxa de aumento: '))
taxa_menos = int(input('Digite a taxa de diminuir: '))
moeda.resumo(valor, taxa_mais, taxa_menos)

