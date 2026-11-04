def commonChars(words):
    common = {}

    for ch in words[0]:
        if ch in common:
            common[ch] += 1
        else:
            common[ch] = 1

    for i in range(1, len(words)):
        freq = {}

        for ch in words[i]:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for ch in common:
            if ch in freq:
                if freq[ch] < common[ch]:
                    common[ch] = freq[ch]
            else:
                common[ch] = 0

    result = []

    for ch in common:
        for i in range(common[ch]):
            result.append(ch)

    return result


words = ["bella", "label", "roller"]

print(commonChars(words))