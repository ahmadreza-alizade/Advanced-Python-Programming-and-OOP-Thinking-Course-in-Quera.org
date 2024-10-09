
p, d = map(int, input().split())

plus = d
while(True):
    reminder = d % p
    if 0 <= reminder <= p//2 :
        print(d)
        break
    else:
        d += plus
        
        
