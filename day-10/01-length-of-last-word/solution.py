def lengthOfLastWord(s):
    i = len(s) - 1

    while i >= 0 and s[i] == ' ':
        i -= 1

    count = 0

    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1

    return count


s = "Hello World"
print(lengthOfLastWord(s))