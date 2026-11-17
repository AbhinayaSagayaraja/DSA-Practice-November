def vowelStrings(words, queries):
    vowels = "aeiou"
    prefix = [0]*(len(words)+1)
    for i in range(len(words)):
        word = words[i]
        if word[0] in vowels and word[-1] in vowels:
            prefix[i+1]=prefix[i] + 1
        else:
            prefix[i+1] = prefix[i]
    result = []
    for q in queries:
        left = q[0]
        right = q[1]
        count = prefix[right+1]-prefix[left]
        result.append(count)

    return result
words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]
print(vowelStrings(words, queries))