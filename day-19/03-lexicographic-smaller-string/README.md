# Lexicographic Smaller String Comparison

## Approach
Compared both strings character by character.
The first different character determines which string
is lexicographically smaller.
If all common characters match, the shorter string is smaller.

## Time Complexity
O(n), where n is the length of the shorter string.

## Space Complexity
O(1)

## Edge Case
If both strings are identical, return 0.