x = 15
name = 'Jorge de Sousa'
b = 'ordem e progresso'

print(len(name))
print(name.count('o'))

x_convertido = float(x) #converter int em float
print(x_convertido)
print(type(x_convertido))
print(name.upper())
print(name.lower())
print(name.replace('Jorge', 'Andressa')) #efetuar troca de nome
print(name)
print(name.startswith('Jorge')) #verificar se inicia com
print(name.endswith('Sousa')) #verifica se termina com
print(b.capitalize()) #fazer com que primeira letra do primeiro nome inicie maiscula
print(name.isdigit())
print(b.isalnum())
print(b[0:3].upper())
print(b[::2].upper()) #imprime os caracteres pares
print(b[1::2]) #imprime os caracteres referentes aos indices impares