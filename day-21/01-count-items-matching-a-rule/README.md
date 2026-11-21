# Count Items Matching a Rule

## Approach
- I check each item based on the given ruleKey.
- I select the corresponding type, color or name.
- If the selected value matches ruleValue, I increase the count.

## Time Complexity
O(n), where n is the number of items.

## Space Complexity
O(1), as no additional data structure is used.

## Edge Case
If no item matches the given rule, the function returns 0.