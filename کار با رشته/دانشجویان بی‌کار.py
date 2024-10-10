import re


def checkreg(result, sharp):
    pattern_start = r"^\d*#"
    pattern_end = r"#\d*$"

    res_start = re.search(pattern_start, sharp)
    res_end = re.search(pattern_end, sharp)

    if res_start and res_end:
        res_start = str(re.search(pattern_start, sharp).group()[0:-1])
        res_end = str(re.search(pattern_end, sharp).group()[1:])
    

        if re.search(fr"^{res_start}.+{res_end}$", result):
            # return(" ".join(el).replace(sharp, result))
            return (True)
    else:
        return (False)


def solve(arr):
    pattern = r"\s+"
    el = re.split(pattern, arr)
    for i in el:
        if "#" in i:
            if el.index(i) == 0:
                result = str(int(el[4]) - int(el[2]))
                if checkreg(result, i):
                    return (" ".join(el).replace(i, result))
                else:
                    return ('-1')

            elif el.index(i) == 2:
                result = str(int(el[4]) - int(el[0]))
                if checkreg(result, i):
                    return (" ".join(el).replace(i, result))
                else:
                    return ('-1')

            elif el.index(i) == 4:
                result = str(int(el[0]) + int(el[2]))
                if checkreg(result, i):
                    return (" ".join(el).replace(i, result))
                else:
                    return ('-1')
        else:
            pass

    print(solve(equition))
