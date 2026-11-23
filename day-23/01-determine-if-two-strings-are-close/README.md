# Determine if Two Strings Are Close

## Approach
- First, I check whether both strings have equal lengths.
- I create frequency dictionaries for both strings.
- Both strings must contain exactly the same distinct characters.
- I compare the frequency counts of both strings.
- If the frequency distributions match, the strings are close.

## Time Complexity
O(n), where n is the length of the strings.

## Space Complexity
O(k), where k is the number of distinct characters.

## Edge Case
If both strings have different characters, they cannot be close even if their lengths are equal.