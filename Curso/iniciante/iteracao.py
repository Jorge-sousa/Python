frase = 'Socorram-me subi em um ônibus em Marrocos'

i = 0

qtd_mais_x = 0
letra_x = ''

while i < len(frase):
    letra_atual = frase[i]
    x_letra_apareceu = frase.count(letra_atual)

    if qtd_mais_x < x_letra_apareceu:
        qtd_mais_x = x_letra_apareceu
        letra_x = letra_atual


    print(letra_atual, x_letra_apareceu)
    i += 1

print('A letra que apareceu mais vezes foi: {}'.format(letra_x))
