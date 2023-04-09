lar = float(input('Qual largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = lar * alt

print('A largura é {} e a altura é {}. O total da área da parede é {:.2f}m²'.format(lar, alt, area))
tinta = area / 2
print('Você vai precisar de {}L de tinta para pintar essa parede'.format(area))

