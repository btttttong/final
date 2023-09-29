

def find_dup(inp):
    counter = dict()
    dup_num = 0
    for i in inp:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    print(counter)
    # return counter

    for item in counter:
        if counter[item] > 2:
            dup_num += 1
    print(dup_num)

find_dup('abcde')
find_dup('aabbcde')

