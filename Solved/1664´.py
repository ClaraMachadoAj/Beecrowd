jogo = (input('input: ').upper()).split('BULLSHIT')

print(jogo)

while True:
    try:
        quant_jogos = len(jogo)
        jogo_separado = str(jogo).split()
        parametro = jogo_separado[0]
        for palavras in jogo_separado:
            if parametro == palavras:
                index = jogo_separado.index(palavras)
                jogo_separado.pop(index)
            else:
                continue
        print(jogo_separado)
    except EOFError:
        break