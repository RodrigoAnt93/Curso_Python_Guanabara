def dia_exten(d):
    d = d.split('/')
    dia = ('Um', "Dois", "Três", 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
         'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte',
         'Vinte e um', 'Vinte e dois', 'Vinte e três', 'Vinte e quatro', 'Vinte e cinco', 'Vinte e seis', 'Vinte e sete',
         'Vinte e oito', 'Vinte e nove', 'Trinta', 'Trinta e um')
    dia_nas = ''




def mes_exten(m):
    mes = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')
    mes_nas = ''
    for i in m[3:5]:
        mes_nas = i
    mes_nas = int(mes_nas)
    if mes_nas > 12:
        return 'MesErro'
    else:
        return mes[mes_nas - 1]


data = str(input('Digite sua data de nascimento [dd/mm/aaaa]: ')).strip()
print(f'{dia_exten(data)} de {mes_exten(data)} de {data[6:]}')
