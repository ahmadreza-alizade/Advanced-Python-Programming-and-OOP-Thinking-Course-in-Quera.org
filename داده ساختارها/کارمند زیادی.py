def main():
    num_names = int(input())
    name_dict = dict()

    for i in range(num_names):
        name = input().split()
        name_dict[name[1]] = name[0]

    values_set = {val for val in name_dict.values()}
    name_counter = {val: 0 for val in values_set}

    for val in name_dict.values():
        if val in values_set:
            name_counter[val] += 1

    max_counters = max([val for val in name_counter.values()])
    print(max_counters)


if __name__ == "__main__":
    main()

# name = dict()
# n = int(input())
# for i in range(n):
#     first, last = input().split()
#     if first in name:
#         name[first] += 1 
#     else:
#         name[first] = 1 
# print(max(list(name.values())))
