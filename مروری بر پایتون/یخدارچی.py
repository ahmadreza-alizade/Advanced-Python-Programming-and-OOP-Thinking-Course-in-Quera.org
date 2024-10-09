#اگر دمای داخل سماور بیش از ۱۰۰ درجه بود، Steam؛ اگر دمای آن زیر ۰ بود، Ice و در غیر این صورت، Water چاپ شود.
temp = int(input())

steam = "Steam"
water = "Water"
ice = "Ice"

if temp > 100:
    print(steam)
elif temp < 0:
    print(ice)
else:
    print(water)
