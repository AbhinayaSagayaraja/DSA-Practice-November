def groupAnagrams(strs):
    groups = {}

    for word in strs:
        freq = [0] * 26

        for ch in word:
            index = ord(ch) - ord('a')
            freq[index] += 1

        key = tuple(freq)

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    result = []

    for group in groups.values():
        result.append(group)

    return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))