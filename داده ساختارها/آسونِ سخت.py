# TODO: Just in one line!
print(*sorted([el for index, el in enumerate(list(map(int, input().split())), start=1) if el%6 == 0 and index%6 == 0]))
