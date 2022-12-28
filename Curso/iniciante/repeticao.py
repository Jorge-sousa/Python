num_01 = 0
num_02 = 0

while num_01 <= 4:
    num_01 += 1
    print(f' Contador Exterior: {num_01}')

    while num_02 <= 9:
        num_02 += 1

        if num_02 == 5:
            print(f'Não Mostrarei o: {num_02:.2f}')
            continue

        print(f'Contador interior: {num_02}')
    if num_02 >= 10:
        num_02 = 0




"""
contador = 0

while contador <= 50:
    contador += 1

    if contador >= 10 and contador <= 25:
        print('Não irei mostrar: ', f'{contador:.2f}')
        continue
    if contador == 20:
        print('Não irei mostrar: ', contador)
        continue
    if contador == 30:
        print('Não irei mostrar: ', contador)
        continue
    if contador == 40:
        print('Não irei mostrar: ', contador)
        continue
    if contador == 50:
        print('Não irei mostrar: ', contador)
        continue

    print(contador)


print('FINALIZADO')



condicao = True

while condicao:
    name = input('Qual o seu nome? ')
    print(f'Nome: {name}')

    if name == 'sair':
        break



num = 0

while num < 10:
    num += 1
    print(f'{num:.2f}')

print('Acabou', '!' * 10, sep='-' * 3)
print('Acabou' * num)

"""