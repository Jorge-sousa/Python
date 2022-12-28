# name = 'Jorge de Sousa'
# age = 27
# name_modify = name.split()

# print(f'{age:.2f}')
# print(name.count('e'))
# print(len(name))
# print(len(name_modify))


def name():
    def name_split(name):
        return name.split()

    return name_split

def list_name(*arg):
    return type(*arg)

def test_list(listing):
    test = listing == list
    return test    

name_utility = name()
print(test_list(list_name(name_utility('Jorge'))))