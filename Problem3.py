def return_middle(inp):
    if len(inp) > 1:
        middle = int(len(inp) / 2)
        mid_str = ''
        if len(inp) % 2 == 0:
            return inp[middle - 1] + inp[middle]
        else:
            return inp[middle]
    else:
        return 'empty string'


print(return_middle('test'))
print(return_middle('testing'))
print(return_middle('middle'))
print(return_middle('0'))
