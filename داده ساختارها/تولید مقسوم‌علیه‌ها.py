
def divs(a: int):
    m = 1
    while(m <= a):
        if a%m == 0:
            yield m
        m += 1

if __name__ == "__main__":
    print(list(divs(4)))    
