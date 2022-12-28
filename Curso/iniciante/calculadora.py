calculator = True

while calculator:

    number_01 = input('Informe um número: ')
    number_02 = input('Informe um segundo número: ')
    operator = input('Informe o operador matemático: ') 

    exit = number_01 == 'exit' or number_02 == 'exit'
    if not exit:
        int_number_01 = int(number_01)
        int_number_02 = int(number_02)

    if exit:
        break

    if operator == '+':
        print(int_number_01 + int_number_02)
    
    if operator == '-':
        print(int_number_01 - int_number_02)

    if operator == '/':
        print(f'{(int_number_01 / int_number_02):.2f}')

    if operator == '*':
        print(int_number_01 * int_number_02)
        