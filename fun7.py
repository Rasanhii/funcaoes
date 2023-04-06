def ano_bi(ano):
    if ano % 4 !=0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True


# anos para comparar
dados_teste = [2005, 2005, 2016, 1987, 2020]

# resultado real
resultados_reais = [False, True, True, False, True]

# cheacr a função
for i in range(len(dados_teste)):
    yr = dados_teste[i]
    print(yr, '-> ', end='')
    result = ano_bi(yr)
    if result == resultados_reais[i]:
        print('OK')
    else:
        print('Falha')
