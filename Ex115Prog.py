from Ex115 import interface
from Ex115 import banco_dados


arq = 'arquivo_cadastro.txt'
if not banco_dados.arquivoExiste(arq):
    banco_dados.criar_arquivo(arq)

while True:
    resp = interface.resposta()
    if resp == 1:
        banco_dados.ler_arquivo(arq)
    elif resp == 2:
        interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = int(input('Idade: '))
        banco_dados.cadastrar(arq, nome, idade)
    elif resp == 3:
        print('tchau')
        break
    else:
        print('\033[1;31mERRO! Opção inválida.\033[m')