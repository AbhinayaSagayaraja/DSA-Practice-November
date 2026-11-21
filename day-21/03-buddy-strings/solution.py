class Solution:
    def buddyStrings(self, s, goal):

        if len(s) != len(goal):
            return False

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        if len(diff) == 2:
            a = diff[0]
            b = diff[1]

            if s[a] == goal[b] and s[b] == goal[a]:
                return True

            return False

        if len(diff) == 0:

            freq = {}

            for ch in s:
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1

            for ch in freq:
                if freq[ch] > 1:
                    return True

        return False


s = Solution()

print(s.buddyStrings("ab", "ba"))
print(s.buddyStrings("ab", "ab"))
print(s.buddyStrings("aa", "aa"))
print(s.buddyStrings("aaaaaaabc", "aaaaaaacb"))