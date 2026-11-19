def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1

    while left <= right:
        mid = (left + right) // 2

        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    if left == len(letters):
        return letters[0]

    return letters[left]


letters = ["c", "f", "j"]
target = "a"

print(nextGreatestLetter(letters, target))