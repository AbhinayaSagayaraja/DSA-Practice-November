
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):

            char1 = s[i]
            char2 = t[i]

            # Check mapping from s to t
            if char1 in s_to_t:
                if s_to_t[char1] != char2:
                    return False
            else:
                s_to_t[char1] = char2

            # Check reverse mapping from t to s
            if char2 in t_to_s:
                if t_to_s[char2] != char1:
                    return False
            else:
                t_to_s[char2] = char1

        return True


# Test cases
solution = Solution()

print(solution.isIsomorphic("egg", "add"))       # True
print(solution.isIsomorphic("foo", "bar"))       # False
print(solution.isIsomorphic("paper", "title"))   # True
