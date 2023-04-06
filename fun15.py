def romano_para_decimal(num_romano):
    valores= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal = 0
    for i in range(len(num_romano)):
        if i > 0 and valores[num_romano[i]] > valores[num_romano[i-1]]:
            decimal += valores[num_romano[i]] -2 * valores[num_romano[i-1]]
        else:
            decimal += valores[num_romano[i]]
    return decimal

num_romano = 'MCMXCIV'
decimal = romano_para_decimal(num_romano)
print(num_romano, 'em decimal', decimal)