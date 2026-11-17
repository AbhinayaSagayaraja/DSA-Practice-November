def countVowelSubstrings(word):
    v = "aeiou"
    cnt = 0

    for i in range(len(word)):
        freq = {}

        for j in range(i, len(word)):
            ch = word[j]

            if ch not in v:
                break

            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

            if len(freq) == 5:
                cnt += 1

    return cnt


word = "aeiouu"
print(countVowelSubstrings(word))