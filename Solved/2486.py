vitamina_C = {'suco de laranja': 120, 'morango fresco': 85, 'mamao': 85, 'goiaba vermelha': 70, 'manga': 56, 'laranja': 50, 'brocolis': 34}

def somando(quant, fruta):
    quant_Vitamina_C = vitamina_C[fruta] * quant
    return quant_Vitamina_C

while True:
    vitamina = 0  # Reset vitamina for each test case
    test_cases = int(input())
    if test_cases == 0:
        break
    for i in range(test_cases):
        entrada = input().split()
        quant = int(entrada[0])
        fruta = ' '.join(entrada[1:])
        vitamina += somando(quant, fruta)

    if vitamina > 130:
        ideal = vitamina - 130
        print(f'Menos {ideal} mg')
    elif vitamina < 110:
        ideal = 110 - vitamina
        print(f'Mais {ideal} mg')
    else:
        print(f'{vitamina} mg')