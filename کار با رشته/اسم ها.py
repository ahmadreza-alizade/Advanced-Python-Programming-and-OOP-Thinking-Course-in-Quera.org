
if __name__ == "__main__":
    case_num = int(input())

    result = max([len(set(input())) for i in range(case_num)])

    print(result)
