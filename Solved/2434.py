dias, saldo = map(int, input().split())
menor = saldo

for _ in range(dias):
    gasto = int(input())
    
    saldo += gasto

    if saldo < menor:
        menor = saldo

print(menor)