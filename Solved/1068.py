def verificador(expressão):
    quant = 0
    for caracter in range(len(expressao)):
        if expressao[caracter] == '(':
            quant += 1 
        elif expressao[caracter] == ')':
            quant -= 1
        
        if quant < 0:
            break
    if quant != 0:
        print('incorrect')
    else:
        print('correct')

while True:
    try:
        expressao = input()
        verificador(expressao)
    except EOFError:
        break
