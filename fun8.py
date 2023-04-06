def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

notas = [7.5, 8.0, 6.5, 9.0]
media = calcular_media(notas)
print('Média é: ', media)