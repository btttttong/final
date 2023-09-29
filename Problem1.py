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

    check_sum_num = (10 - sumi % 10) % 10
    return check_sum_num


print(check_sum('7992739871'))
print(check_sum('62'))
