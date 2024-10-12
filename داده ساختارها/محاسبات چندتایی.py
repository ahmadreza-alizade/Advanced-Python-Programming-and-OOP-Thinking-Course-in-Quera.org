def calc(a: list) -> tuple:
    max_l = max(a)
    avg_l = sum(a) / len(a)
    a.sort()
    if len(a) % 2 == 0:
        idx1 = len(a) // 2 - 1
        idx2 = idx1 + 1
        m_l = (a[idx1] + a[idx2]) / 2
    else:
        idx = len(a) // 2
        m_l = a[idx]

    t = (avg_l, m_l, max_l)
    return (t)
# from statistics import mean, median

# def calc(a: list) -> tuple:
#     avg = mean(a)  # محاسبه میانگین
#     med = median(a)  # محاسبه میانه
#     max_value = max(a)  # محاسبه بزرگترین عدد

#     return (avg, med, max_value)  # بازگشت یی

if __name__ == "__main__":
    print(calc([2, 20, 30, 29]))
