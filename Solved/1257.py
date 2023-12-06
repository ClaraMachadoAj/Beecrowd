test_cases = int(input())

for _ in range(test_cases):
    valor = 0
    quantity = int(input())

    for i in range(quantity):
        frase = input()

        for j in range(len(frase)):
            valor += ord(frase[j]) - ord('A') + i + j
    
    print(valor)