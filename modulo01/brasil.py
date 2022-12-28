def jogo_01(time_03 = 'Suíça', time_04 = 'Camarões'):
    while True:
        pontos_suica = 0
        pontos_camaroes = 0
        print('RODADA 01: SUÍÇA x CAMARÕES')
        gols_suica = input('Informe quantos gols fez a Suíça: ')

        if gols_suica.isdigit():
            gols_suica_int = int(gols_suica)
            gols_camaroes = input('Informe quantos gols fez Camarões: ')

            if gols_camaroes.isdigit():
                gols_camaroes_int = int(gols_camaroes)
                if gols_suica > gols_camaroes:
                    pontos_suica += 3
                    print(f'SUÍÇA {gols_suica} x {gols_camaroes} CAMARÕES. \n')

                elif gols_suica < gols_camaroes:
                    pontos_camaroes += 3
                    print(f'SUÍÇA {gols_suica} x {gols_camaroes} CAMARÕES\n')

                else:
                    pontos_suica += 1
                    pontos_camaroes += 1
                    print(f'SUÍÇA {gols_suica} x {gols_camaroes} CAMARÕES\n')

            else:
                print('Informe um valor válido: ')
                

        else:
            print('Informe um valor válido: ')

        saldo_suica = gols_suica_int - gols_camaroes_int 
        saldo_camaroes = gols_camaroes_int - gols_suica_int        
           

        break


    def jogo_02(time_01 = 'Brasil', time_02 = 'Sérvia'):
        while True:
            pontos_brasil = 0
            pontos_servia = 0

            print('RODADA 01: BRASIL x SÉRVIA')
            gols_brasil = input('Informe quantos gols fez o Brasil: ')

            if gols_brasil.isdigit():
                gols_brasil_int = int(gols_brasil)
                gols_servia = input('Informe quantos gols fez a Sérvia: ')

                if gols_servia.isdigit():
                    gols_servia_int = int(gols_servia)
                    if gols_brasil > gols_servia:
                        pontos_brasil += 3
                        print(f'BRASIL {gols_brasil} x {gols_servia} SÉRVIA. \n')

                    elif gols_brasil < gols_servia:
                        pontos_servia += 3
                        print(f'BRASIL {gols_brasil} x {gols_servia} SÉRVIA. \n')

                    else:
                        pontos_brasil += 1
                        pontos_servia += 1
                        print(f'BRASIL {gols_brasil} x {gols_servia} SÉRVIA. \n')

                else:
                    print('Informe um valor válido: ')
                    

            else:
                print('Informe um valor válido: ')

            saldo_brasil = gols_brasil_int - gols_servia_int 
            saldo_servia = gols_servia_int - gols_brasil_int    

            print('Pontos da Suiça: ', pontos_suica)
            print('Pontos Camarões: ', pontos_camaroes)
            print('Saldo Suíça: ', saldo_suica)
            print('Saldo Camarões: ', saldo_camaroes)
            print('Pontos do Brasil: ', pontos_brasil)
            print('Pontos da Sérvia: ', pontos_servia)
            print('Saldo Brasil: ', saldo_brasil)
            print('Saldo Sérvia: ', saldo_servia)
            

            break
    
    jogo_02()
jogo_01()
