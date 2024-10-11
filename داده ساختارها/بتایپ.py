
if __name__ == '__main__':
    s = input()
    s_list = list(s)
    s_stack = list()
    for el in s_list:
        if el != "=":
            s_stack.append(el)
        elif len(s_stack) != 0:
            s_stack.pop()
            
    print("".join(s_stack))
