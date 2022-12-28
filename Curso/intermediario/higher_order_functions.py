def func01(x):
    def func02(y):
        return x + y
    return func02

variable = func01(5)
print(variable(2))

# def my_name(name):
#     return f'Hi {name}'

# def sr_name(name):
#     return name.upper()

# def welcome(name):
#     return f'{name}, seja bem vindo'

# print(my_name(welcome(sr_name('Jorge'))))

# def number(x):
#     def div():
#         return x % 2 == 0
#     return div

# pair = number(2)
# print(pair())


# def mult_func(number1):
#     def mult(number2):
#         return number1 * number2
#     return mult

# multiplied = mult_func(2)
# print(multiplied(5))


# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend

# divide = divisor(2)
# print(divide(10))


# def greet(name):
#     return f'Hi {name}'

# def Upper(name):
#     return name.upper()

# def Lower(name):
#     return name.lower()


# print(greet(Upper('Jorge')))

# def number(num1):
#     return num1

# def div(num1):
#     return num1 / 2

# def mult(num1):
#     return num1 * 2

# number_one = number
# print(number_one(mult(5)))
# print(10*2)