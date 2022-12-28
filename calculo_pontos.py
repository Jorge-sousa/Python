 def jogo_02(time_01 = 'Brasil', time_02 = 'Suíça'):
        while True:
            pontos_brasil = 0
            pontos_suica = 0

            print('RODADA 01: BRASIL x SUÍÇA')
            gols_brasil = input('Informe quantos gols fez o Brasil: ')

            if gols_brasil.isdigit():
                gols_brasil_int = int(gols_brasil)
                gols_suica = input('Informe quantos gols fez a Suíça: ')

                if gols_suica.isdigit():
                    gols_suica_int = int(gols_suica)
                    if gols_brasil > gols_suica:
                        pontos_brasil += 3
                        print(f'BRASIL {gols_brasil} x {gols_suica} SUÍÇA. \n')

                    elif gols_brasil < gols_suica:
                        pontos_suica += 3
                        print(f'BRASIL {gols_brasil} x {gols_suica} SUÍÇA. \n')

                    else:
                        pontos_brasil += 1
                        pontos_suica += 1
                        print(f'BRASIL {gols_brasil} x {gols_suica} SUÍÇA. \n')

                else:
                    print('Informe um valor válido: ')
                    

            else:
                print('Informe um valor válido: ')

            saldo_brasil = gols_brasil_int - gols_suica_int 
            saldo_suica = gols_suica_int - gols_brasil_int 
