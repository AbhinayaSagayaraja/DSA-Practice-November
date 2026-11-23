class Solution:
    def minOperations(self, s):

        count1 = 0
        count2 = 0

        for i in range(len(s)):

            if i % 2 == 0:
                if s[i] != "0":
                    count1 += 1
            else:
                if s[i] != "1":
                    count1 += 1

            if i % 2 == 0:
                if s[i] != "1":
                    count2 += 1
            else:
                if s[i] != "0":
                    count2 += 1

        if count1 < count2:
            return count1

        return count2


s = Solution()

print(s.minOperations("0100"))
print(s.minOperations("10"))
print(s.minOperations("1111"))