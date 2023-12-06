
quantAbas, acoes = map(int, input().split())

for i in range(acoes):
    acao = input().lower()

    if acao == 'fechou':
        quantAbas += 1
    elif acao == 'clicou':
        quantAbas -= 1
    else:
        break

print(quantAbas)