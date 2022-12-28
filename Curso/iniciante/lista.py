#Métodos uteis: append, insert, pop, del, clear, extend
#CRUD = Create, Read, Update, Delete

cafe = ['café', 'Pão']
breakfast = ['Rice', 'Bean', 'Meat', 'Juice', 'Juice']


cafe.append('Leite') # adiciona um elemento ao final da lista
cafe.append('Queijo')
cafe.insert(1, 'Biscoito') # adiciona um elemento, passa o indice e o elemento a ser adicionado

del cafe[-1] # Deleta um elemento da lista, passando o -1 irá deletar o último
elemtent_remove = cafe.pop() # remove o último elemento da lista

print(cafe[0].upper())
print(cafe[1].lower().startswith('p'))
print(cafe[1].endswith('o'))
print(len(cafe))
print('Elemento removido = {}'.format(elemtent_remove))

tamanho = len(cafe)
cafe.insert(tamanho, 'Abobrinha')
print(cafe)
print(tamanho)

print(breakfast.count('Juice'))
