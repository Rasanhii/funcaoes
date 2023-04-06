def verifica_primo(numero):
    if numero <2:
        return False
    for i in range(2, int(numero/2) + 1):
        if numero % i == 0:
            return False
    return True

while True:    
    numero = int(input('Insira um números: '))
    if verifica_primo(numero):
        print('{} é primo'.format(numero))
    else:
        print('{} não é primo'.format(numero))
    
    fim = input('Deseja usar o programa denovo? (s ou n) \nResp: ')
    if fim == 'n':
        break

print('Obrigado por usar o programa!')