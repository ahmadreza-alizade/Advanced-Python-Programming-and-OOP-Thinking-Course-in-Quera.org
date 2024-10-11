# TODO: Just in one line!
if __name__ == "__main__":
    print(*sorted([el for index, el in enumerate(list(map(int, input().split())), start=1) if el%6 == 0 and index%6 == 0]))

# print(*sorted(x for x in list(map(int, input().split()))[5::6]if (x % 2) == 0 and (x % 3) == 0))

