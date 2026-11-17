def sumPrefixScores(words):
    trie = {}

    for word in words:
        node = trie

        for ch in word:
            if ch not in node:
                node[ch] = {"cnt": 0}

            node = node[ch]
            node["cnt"] += 1

    res = []

    for word in words:
        node = trie
        score = 0

        for ch in word:
            node = node[ch]
            score += node["cnt"]

        res.append(score)

    return res


words = ["abc", "ab", "bc", "b"]
print(sumPrefixScores(words))