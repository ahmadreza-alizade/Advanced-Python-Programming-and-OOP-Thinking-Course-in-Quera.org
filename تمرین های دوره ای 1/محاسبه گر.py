def odd_or_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def chess_cal(ls : list) -> int:
    total_num = 0
    for i in range(0, len(ls)):
        if odd_or_even(i):
            total_num += ls[i]
        else:
            total_num -= ls[i]
    return total_num



def calculator(n, m, ls):
    final_list = []
    mod = n % m
    kh_qesmat = n // m 

    for i in range(0, kh_qesmat):
        total = 0
        for j in range(0, m):
            total += ls.pop(0)
        final_list.append(total)

    if mod != 0:

        final_list.append(sum(ls))
    # print(final_list)
    result = chess_cal(final_list)
    # print(result)
    return result



# Local Tests
print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
# print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))

