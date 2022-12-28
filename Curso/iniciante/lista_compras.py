market = []

while True:
    acao = input('Informe se deseja listar[L], Inserir[I] ou Excluir[E] a lista: \n').lower()

    if acao == 'i':
        item = input('Informe o item que deseja adicionar a lista: \n')
        market.append(item)
        continue

    elif acao == 'l':
        print(market)
        continue

    elif acao == 'e':
        excluir = input('Informe o item que deseja excluir da lista: \n')
        item_excluir = market.count(excluir)

        if item_excluir > 0:
            i = market.index(excluir)
            print('Excluindo: ', excluir)
            del market[i]

        else:
            print('Não foi encontrado o item especificado em sua lista de compras.\n')
        continue
    
    else: 
        print('Informe uma opção válida: listar[L], Inserir[I] ou Excluir[E]\n')