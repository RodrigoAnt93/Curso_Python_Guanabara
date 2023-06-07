s1 = str(input('Digite a primeira frase: ')).strip().upper()
s2 = str(input('Digite a segunda frase: ')).strip().upper()
print('A primeira frase tem {} caracteres'.format(len(s1)))
print('A segunda frase tem {} caracteres'.format(len(s2)))
if len(s1) == len(s2):
    s1 = s1.split()
    s1 = ''.join(s1)
    s2 = s2.split()
    s2 = ''.join(s2)
    if s1 == s2:
        print('''Essas duas frases tem tamanhos e conteúdos iguais.''')
    else:
        print('Essa frase tem tamanho iguais.')
elif s1 != s2:
    s1 = s1.split()
    s1 = ''.join(s1)
    s2 = s2.split()
    s2 = ''.join(s2)
    if s1 == s2:
        print('Essas frases são de tamanhos diferentes, mas de conteudo iguais.')
    else:
        print('Essas frases são de tamanhos e conteúdos diferentes.')

