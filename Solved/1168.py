test_cases = int(input())
led = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}



for quant_de_vezes in range(test_cases):
    quant_led = list(input())
    soma = 0
    
    for andando_na_biblioteca in quant_led:
        soma += led[andando_na_biblioteca]

    print(f'{soma} leds')



