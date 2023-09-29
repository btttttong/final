def rec_sum(listinp):
    if len(listinp) == 0:
        return 0
    else:
        return listinp[0] + rec_sum(listinp[1:])

print(rec_sum([1, 2, 5, 5]))
