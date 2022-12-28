# sets have no indexes

#sets eliminate duplicate data 
set_one = {12, 11, 12, 13, 14, 14}
print(set_one)

for number in set_one:
    print(number)
    if number == 13:
        print('Thirteen found')
    else:
        print('Thirtenn not found')