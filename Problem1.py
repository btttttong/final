import math


def check_sum(number):
    check_sum_num = 0
    reverse_num = number[::-1]
    sumi = 0

    resi = 0
    for i in range(len(reverse_num)):
        if i % 2 == 0 or i == 0:
            resi = int(reverse_num[i]) * 2
        else:
            resi = int(reverse_num[i]) * 1

        if resi > 10:
            resi = resi - 9

        sumi += resi

    print(sumi)
    if sumi == 10:
        check_sum_num = 0
    else:
        check_sum_num = 10 - sumi%10
    print(check_sum_num)
    return check_sum_num


check_sum('7992739871')
check_sum('62')
