class Solution:
    def isPrefixOfWord(self, sentence, searchWord):

        word_no = 1
        word = ""

        for i in range(len(sentence) + 1):

            if i == len(sentence) or sentence[i] == " ":

                if len(searchWord) <= len(word):

                    match = True

                    for j in range(len(searchWord)):
                        if word[j] != searchWord[j]:
                            match = False
                            break

                    if match:
                        return word_no

                word = ""
                word_no += 1

            else:
                word += sentence[i]

        return -1


s = Solution()

print(s.isPrefixOfWord("i love eating burger", "burg"))
print(s.isPrefixOfWord("this problem is easy", "pro"))
print(s.isPrefixOfWord("i am tired", "you"))
print(s.isPrefixOfWord("hello from the other side", "they"))