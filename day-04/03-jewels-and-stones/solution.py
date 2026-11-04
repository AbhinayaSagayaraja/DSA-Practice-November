def numJewelsInStones(jewels, stones):
    freq = {}

    for ch in stones:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    count = 0

    for ch in jewels:
        if ch in freq:
            count += freq[ch]

    return count


jewels = "aA"
stones = "aAAbbbb"

print(numJewelsInStones(jewels, stones))