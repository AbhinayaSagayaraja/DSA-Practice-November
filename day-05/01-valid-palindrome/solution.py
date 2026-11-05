def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not (
            ('a' <= s[left] <= 'z') or
            ('A' <= s[left] <= 'Z') or
            ('0' <= s[left] <= '9')
        ):
            left += 1

        while left < right and not (
            ('a' <= s[right] <= 'z') or
            ('A' <= s[right] <= 'Z') or
            ('0' <= s[right] <= '9')
        ):
            right -= 1

        a = s[left]
        b = s[right]

        if 'A' <= a <= 'Z':
            a = chr(ord(a) + 32)

        if 'A' <= b <= 'Z':
            b = chr(ord(b) + 32)

        if a != b:
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))