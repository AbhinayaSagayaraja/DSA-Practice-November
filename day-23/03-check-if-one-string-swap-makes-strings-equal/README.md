# Check If One String Swap Can Make Strings Equal

## Approach
- First, I check whether both strings have equal lengths.
- I store the positions where the characters differ.
- If there are no differences, the strings are already equal.
- If exactly two positions differ, I check whether swapping those characters makes the strings equal.
- Any other number of differences returns False.

## Time Complexity
O(n), where n is the length of the strings.

## Space Complexity
O(1), because at most two mismatch positions are stored.

## Edge Case
If both strings are already equal, the answer is True because zero swaps are allowed.