def fahrenheit_para_celsius(temp_f):
    temp_c = (temp_f -32) * 5/9
    return temp_c

temp_f = 75
temp_c = fahrenheit_para_celsius(temp_f)
print('{} graus Fahrenheit equivalem a {}'.format(temp_f, temp_c))
temp_c_arredondado = round(temp_c, 1)
print('{} graus Fahrenheit equivalem a {}'.format(temp_f, temp_c_arredondado))