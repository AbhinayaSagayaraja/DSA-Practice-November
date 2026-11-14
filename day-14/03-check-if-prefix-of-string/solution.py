
class Solution:
    def longestCommonSuffix(self, strs: list[str]) -> str:

        if not strs:
            return ""

        suffix = ""

        # Take the first string as the reference
        first = strs[0]

        # Start checking from the last character
        for i in range(1, len(first) + 1):

            char = first[-i]

            # Compare with every other string from the end
            for j in range(1, len(strs)):

                if i > len(strs[j]) or strs[j][-i] != char:
                    return suffix

            suffix = char + suffix

        return suffix


# Test cases
solution = Solution()

print(solution.longestCommonSuffix(["running", "jogging", "walking"]))
# Output: ing

print(solution.longestCommonSuffix(["flower", "power", "tower"]))
# Output: ower

print(solution.longestCommonSuffix(["apple", "banana", "orange"]))
# Output:
