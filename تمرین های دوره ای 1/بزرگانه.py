def cap_word(word):
    word = word.lower()
    word = word[0].upper() + word[1:]
    return (word)


def cap_ls(ls):
    new_ls = []
    for name in ls:
        new_ls.append(cap_word(name))
    return (" ".join(new_ls))


def capitalize(names):
    names = [cap_ls(name.split(" ")) for name in names]
    return names
