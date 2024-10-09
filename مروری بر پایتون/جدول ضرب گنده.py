#، برنامه‌ای بنویسید که با گرفتن 
# n از ورودی،
# جدول ضرب اعداد ۱ تا 
# n
# را چاپ کند

n = int(input())

for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        print(i * j, end=" ")
    print("\n")
