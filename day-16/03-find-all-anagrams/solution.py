def findAnagrams(s, p):
    n = len(s)
    m = len(p)
    if m > n:
        return []
    target = {}
    window = {}
    for ch in p:
        if ch in target:
            target[ch] += 1
        else:
            target[ch] = 1
    for i in range(m):
        ch = s[i]
        if ch in window:
            window[ch] += 1
        else:
            window[ch] = 1
    result = []
    if window == target:
        result.append(0)
    for right in range(m, n):
        # Addnew character
        ch = s[right]
        if ch in window:
            window[ch] += 1
        else:
            window[ch] = 1
        # Remove the character
        old = s[right - m]

        window[old] -= 1
        if window[old] == 0:
            del window[old]

        if window == target:
            result.append(right - m + 1)
    return result
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))