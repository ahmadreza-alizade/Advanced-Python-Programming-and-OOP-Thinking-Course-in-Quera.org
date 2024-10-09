import math

x_deg = int(input())

first_num = math.ceil(math.pow(x_deg, 5/3) + math.tan(math.radians(x_deg)))
second_num = math.floor(math.pow(math.pi, 2+math.atan(math.pow(math.sin(math.radians(x_deg)), 2))))
                                    
print(math.gcd(first_num, second_num))
