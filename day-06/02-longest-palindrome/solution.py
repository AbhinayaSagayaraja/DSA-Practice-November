def longestPalindrome(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    length = 0
    has_odd = False

    for ch in freq:
        if freq[ch] % 2 == 0:
            length += freq[ch]
        else:
            length += freq[ch] - 1
            has_odd = True

    if has_odd:
        length += 1

    return length


s = "abccccdd"
print(longestPalindrome(s))