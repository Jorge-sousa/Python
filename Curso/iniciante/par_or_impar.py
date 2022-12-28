num_1 =  input('Digite um número inteiro: ')


validacao = num_1.isdigit()

if validacao:
    int_num_1 = int(num_1)
    par = int_num_1 % 2 == 0

    if par:
        print('Você digitou um número par.')


    else:
        print('Você digitou um número ímpar.')

else:
    print('Você não digitou um número inteiro.')    
