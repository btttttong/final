def return_middle(inp):
    if len(inp) > 1:
        middle = int(len(inp) / 2)
        mid_str = ''
        if len(inp) % 2 == 0:
            print(inp[middle - 1] + inp[middle])
            return inp[middle - 1] + inp[middle]
        else:
            print(inp[middle])
            return inp[middle]
    else:
        return 'empty string'


return_middle('test')
return_middle('testing')
return_middle('middle')
return_middle('0')
