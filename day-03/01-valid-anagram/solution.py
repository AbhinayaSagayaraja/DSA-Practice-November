def isAnagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in t:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] < 0:
            return False

    return True


s = "anagram"
t = "nagaram"

print(isAnagram(s, t))