name = 'Jorge'
new_str = ""

n = 0
size = len(name)

while n < size:
    letra = name[n]
    new_str += f'*{letra}'
    n += 1
    

print(new_str)
