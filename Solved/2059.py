def analise_do_jogo(escolha_do_jogador1, num_jogo1, num_jogo2, roubo, acusacao):

    if((roubo == '1') and (acusacao == '1')):
        print('Jogador 2 ganha!')

    elif((roubo == '1') or (acusacao == '1')):
        print('Jogador 1 ganha!')

    else:

        resultado = (int(num_jogo1) + int(num_jogo2)) % 2

        if resultado == '0':

            if escolha_do_jogador1 == '1':
                print('Jogador 1 ganha!')

            else:
                print('Jogador 2 ganha!')

        elif(resultado == int(escolha_do_jogador1)):
            print('Jogador 2 ganha!')

        else:
            print('Jogador 1 ganha!')




escolha_do_jogador1, num_jogo1, num_jogo2, roubo, acusacao = input().split()

analise_do_jogo(escolha_do_jogador1, num_jogo1, num_jogo2, roubo, acusacao)

