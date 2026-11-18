def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def reorganizeString(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    arr = []

    for ch in freq:
        arr.append((ch, freq[ch]))

    arr = mergeSort(arr)

    n = len(s)

    if len(arr) > 0 and arr[0][1] > (n + 1) // 2:
        return ""

    result = [""] * n
    index = 0

    for ch, count in arr:
        for i in range(count):
            if index >= n:
                index = 1

            result[index] = ch
            index += 2

    return "".join(result)


s = "aab"
print(reorganizeString(s))