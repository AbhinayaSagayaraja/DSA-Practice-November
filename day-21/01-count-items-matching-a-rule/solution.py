class Solution:
    def countMatches(self, items, ruleKey, ruleValue):

        count = 0

        for item in items:

            if ruleKey == "type":
                value = item[0]
            elif ruleKey == "color":
                value = item[1]
            else:
                value = item[2]

            if value == ruleValue:
                count += 1

        return count


s = Solution()

items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"]
]

print(s.countMatches(items, "color", "silver"))
print(s.countMatches(items, "type", "phone"))