i = 3
j = 10

def sum_function(i, j=None, k=None):
    j = 11
    i = 2
    sum = i + j + k
    print(f'{i=}, {j=}, {k=} -> ', sum)

    def sub_function(i, j, k):
        k = 3
        sub = i - j - k
        print(f'{i=}, {j=}, {k=}', sub)

    sub_function(i, j, k)
    
sum_function(i, j, 5)
print(j)