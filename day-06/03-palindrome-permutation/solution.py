def canPermutePalindrome(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    odd_count = 0

    for ch in freq:
        if freq[ch] % 2 != 0:
            odd_count += 1

    return odd_count <= 1


s = "code"
print(canPermutePalindrome(s))