cell = {
        'iphone 13': 3800,
        'samsung s22': 4000,
        'xiaomi note 10': 1350
    }

notebook = {
        'dell': 3300,
        'samsung': 2700,
        'lenovo': 2100,
        'acer': 1850 
    }

cells = tuple(cell.items())
notebooks = tuple(notebook.items())

print(cells[0][1])






# group_g = {}


# group_g['team one'] = 'Brazil'
# group_g['team two'] = 'Serbia'

# print(group_g)

# if group_g.get('team one', None) is None:
#     print('Not Exist')
# else:
#     print(group_g['team one'])

# # len = returns the number of keys in the dictionary
# print(len(group_g))

# #returns the keys in the dictionary
# print(group_g.keys())

# #returns keys in a list
# key_list = list(group_g.keys())
# print(key_list[1])

# #returns values from the dictionary
# dictionary_values = group_g.values()

# #returns keys and values from the dictionary
# values_dict = group_g.items()

# for keys, values in group_g.items():
#     print(keys,': ', values)

# group_g.setdefault('team three', 'Cameroon')
# print(group_g)