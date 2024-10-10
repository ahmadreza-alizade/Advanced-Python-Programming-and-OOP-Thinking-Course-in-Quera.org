import re

if __name__ == '__main__':
    my_list = list()
    while (True):
        input_num = int(input())
        if input_num != 0:
            my_list.append(input_num)
        else:
            break

    my_list.reverse()
    [print(i) for i in my_list]
