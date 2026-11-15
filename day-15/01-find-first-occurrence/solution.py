def strStr(h, n):
    a = len(h)
    b = len(n)
    if b== 0:
        return 0
    for i in range(a - b + 1):
        j= 0
        while j < b and h[i + j] == n[j]:
            j+= 1
        if j== b:
            return i
    return -1
h ="sadbutsad"
n ="sad"
print(strStr(h, n))