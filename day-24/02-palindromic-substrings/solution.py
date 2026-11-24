class Solution:
    def shortestPalindrome(self, s):

        end = len(s)

        while end > 0:

            left = 0
            right = end - 1
            is_palindrome = True

            while left < right:

                if s[left] != s[right]:
                    is_palindrome = False
                    break

                left += 1
                right -= 1

            if is_palindrome:
                break

            end -= 1

        remaining = s[end:]

        return remaining[::-1] + s


s = Solution()

print(s.shortestPalindrome("aacecaaa"))
print(s.shortestPalindrome("abcd"))
print(s.shortestPalindrome("a"))