from math import floor, ceil, radians, pi, sin, tan, atan, gcd, pow

x_deg = int(input())

first_num = ceil(pow(x_deg, 5/3) + tan(radians(x_deg)))
second_num = floor(pow(pi, 2+atan(pow(sin(radians(x_deg)), 2))))
                                    
print(gcd(first_num, second_num))
