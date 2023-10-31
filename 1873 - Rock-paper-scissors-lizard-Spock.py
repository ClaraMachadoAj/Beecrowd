quant = int(input())

jogo = {'pedra': ['tesoura', 'lagarto'], 'papel': ['pedra', 'spock'], 'tesoura': ['papel', 'lagarto'], 'lagarto': ['papel', 'spock'], 'spock': ['pedra', 'tesoura']}

for i in range(quant):
    rajesh, sheldon = map(str, input().split())

    if rajesh == sheldon:
        print('empate')
    elif sheldon in jogo[rajesh]:
        print('rajesh')
    else:
        print('sheldon')
