frase = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in frase:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Essa expressão é válida')
else:
    print('Essa expressão é inválida.')