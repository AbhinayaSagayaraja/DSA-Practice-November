class Solution:
    def countWords(self, s):

        count = 0
        inside = False

        for ch in s:

            if ch.isspace():
                inside = False

            else:
                if inside == False:
                    count += 1

                inside = True

        return count


s = Solution()

print(s.countWords("Hello World"))
print(s.countWords("  Python   is fun  "))
print(s.countWords(""))