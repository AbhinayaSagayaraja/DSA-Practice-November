def shortestToChar(s, c):
    n = len(s)
    result = [0] * n

    prev = -n

    for i in range(n):
        if s[i] == c:
            prev = i

        result[i] = i - prev

    prev = 2 * n

    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev = i

        distance = prev - i

        if distance < result[i]:
            result[i] = distance

    return result


s = "loveleetcode"
c = "e"

print(shortestToChar(s, c))