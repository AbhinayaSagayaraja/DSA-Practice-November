def isLetter(ch):
    return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')


def reverseOnlyLetters(s):
    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:

        if not isLetter(chars[left]):
            left += 1

        elif not isLetter(chars[right]):
            right -= 1

        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)


s = "ab-cd"
print(reverseOnlyLetters(s))