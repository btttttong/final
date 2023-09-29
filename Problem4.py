

def find_dup(inp):
    counter = dict()
    dup_num = 0
    for i in inp:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    # print(counter)
    for item in counter.values():
        if item >= 2:
            dup_num += 1

    return dup_num

print(find_dup('ABBA'))

