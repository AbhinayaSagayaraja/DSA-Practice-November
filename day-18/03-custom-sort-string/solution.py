def customSortString(order, s):
    freq = {}
    seen = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    result = []

    for ch in order:
        seen[ch] = True

        if ch in freq:
            for i in range(freq[ch]):
                result.append(ch)

    for ch in freq:
        if ch not in seen:
            for i in range(freq[ch]):
                result.append(ch)

    return "".join(result)


order = "cba"
s = "abcd"

print(customSortString(order, s))