class Solution:
    def closeStrings(self, word1, word2):

        if len(word1) != len(word2):
            return False

        freq1 = {}
        freq2 = {}

        for ch in word1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1

        for ch in word2:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1

        if len(freq1) != len(freq2):
            return False

        for ch in freq1:
            if ch not in freq2:
                return False

        count1 = {}
        count2 = {}

        for ch in freq1:
            value = freq1[ch]

            if value in count1:
                count1[value] += 1
            else:
                count1[value] = 1

        for ch in freq2:
            value = freq2[ch]

            if value in count2:
                count2[value] += 1
            else:
                count2[value] = 1

        return count1 == count2


s = Solution()

print(s.closeStrings("abc", "bca"))
print(s.closeStrings("a", "aa"))
print(s.closeStrings("cabbba", "abbccc"))