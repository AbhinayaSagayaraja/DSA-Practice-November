# Palindromic Substrings

## Approach
- I consider each character as the centre of a palindrome.
- I expand outwards while both characters are equal.
- I count every palindrome found during expansion.
- I check both odd-length and even-length palindromes.

## Time Complexity
O(n^2), where n is the length of the string.

## Space Complexity
O(1), as only a counter and pointers are used.

## Edge Case
If the string contains one character, the count is 1.