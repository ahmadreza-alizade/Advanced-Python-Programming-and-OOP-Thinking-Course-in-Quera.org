# TODO: Just in one line!
print(*sorted([el for index, el in enumerate(list(map(int, input().split()))) if el%6 == 0 and (index+1)%6 == 0]))
