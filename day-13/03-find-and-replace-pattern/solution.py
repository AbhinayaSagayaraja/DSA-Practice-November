
class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:

        result = []

        for word in words:

            if len(word) != len(pattern):
                continue

            word_to_pattern = {}
            pattern_to_word = {}

            is_match = True

            for i in range(len(word)):

                char1 = word[i]
                char2 = pattern[i]

                # Check word-to-pattern mapping
                if char1 in word_to_pattern:
                    if word_to_pattern[char1] != char2:
                        is_match = False
                        break
                else:
                    word_to_pattern[char1] = char2

                # Check pattern-to-word mapping
                if char2 in pattern_to_word:
                    if pattern_to_word[char2] != char1:
                        is_match = False
                        break
                else:
                    pattern_to_word[char2] = char1

            if is_match:
                result.append(word)

        return result


# Test cases
solution = Solution()

print(solution.findAndReplacePattern(
    ["abc", "deq", "mee", "aqq", "dkd", "ccc"],
    "abb"
))  # ['mee', 'aqq']

print(solution.findAndReplacePattern(
    ["a", "b", "c"],
    "a"
))  # ['a', 'b', 'c']
