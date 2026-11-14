
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""

        prefix = ""

        # Take the first string as the reference
        first = strs[0]

        for i in range(len(first)):

            char = first[i]

            # Compare this character with every other string
            for j in range(1, len(strs)):

                # If the string is shorter or character differs
                if i >= len(strs[j]) or strs[j][i] != char:
                    return prefix

            prefix += char

        return prefix


# Test cases
solution = Solution()

print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
# Output: fl

print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
# Output:

print(solution.longestCommonPrefix(["apple", "application", "apply"]))
# Output: appl
