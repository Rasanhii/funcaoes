# palindromo - palavra ou frase que se pode ler,
# indiferentimente, da esquerda para a direita
# ou vice-versa

def verificar_palindromo(texto):
    texto = texto.lower().replace(' ', '')
    return texto == texto[::-1]

# texto (::-1) inverte o texto

texto = 'Socorram me subi no onibus em Marrocos'
if verificar_palindromo(texto):
    print(texto, 'é um palindromo')
else:
    print(texto, 'não é um palindromo')