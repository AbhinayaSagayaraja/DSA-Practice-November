def compareStrings(s1, s2):
    i = 0

    while i < len(s1) and i < len(s2):

        if s1[i] < s2[i]:
            return -1

        elif s1[i] > s2[i]:
            return 1

        i += 1

    if len(s1) < len(s2):
        return -1

    elif len(s1) > len(s2):
        return 1

    return 0


s1 = "apple"
s2 = "banana"

result = compareStrings(s1, s2)

if result == -1:
    print(s1)
elif result == 1:
    print(s2)
else:
    print("Both strings are equal")