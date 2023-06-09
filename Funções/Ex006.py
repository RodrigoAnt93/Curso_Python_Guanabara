hora = 17
minu = 43

if hora <= 12:
    print(f'{hora}:{minu}AM')
elif 12 < hora <= 24:
    print(f'{hora - 12}:{minu}PM')
