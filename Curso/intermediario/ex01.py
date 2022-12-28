def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total

multiplication = multiply(10, 2, 3, 4, 5)
#print(multiplication)

def pair_or_odd(number):
    multiple_of_two = number % 2 == 0

    if multiple_of_two:
        return f'{number} is pair'
    
    return f'{number} is odd'

print(pair_or_odd(2))
print(pair_or_odd(3))
print(pair_or_odd(4))
print(pair_or_odd(5))
print(pair_or_odd(73))
