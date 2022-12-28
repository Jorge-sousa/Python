produtos = ['café', 'arroz', 'feijão', 'carne', 'leite']
produto = ""



while produto != '0':
    produto = input('Informe o produto: ').lower()

    if produto == 'café' or 'cafe' or 'Cafe' or 'Café':
        total = 14
    elif produto == 'arroz' or 'Arroz':
        total = 25
    elif produto == 'feijão' or 'Feijão' or 'Feijao' or 'feijao':
        total = 10
    elif produto == 'carne' or 'Carne':
        total = 45
    elif produto == 'leite' or 'Leite':
        total = 7.5
    else:
        print('Produto não se encontra cadastrado.')

    