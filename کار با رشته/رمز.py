def check_charkhan(pswd, charkhan):
    charkhan_length = 9
    charkhan_starter = 0
    move = min(abs(charkhan.find(pswd) - charkhan_length),
               abs(charkhan_starter - charkhan.find(pswd)))

    return (move)


if __name__ == "__main__":
    case_num = int(input())
    password = list(input())
    charkhanha = [input() for ch in range(case_num)]

    cases = list(zip(password, charkhanha))
    result = sum([check_charkhan(*case) for case in cases])
    print(result)
