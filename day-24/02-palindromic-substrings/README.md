# Shortest Palindrome

## Approach
- I find the longest palindromic prefix of the string.
- I check prefixes from the full string towards shorter lengths.
- I reverse the remaining suffix and add it to the beginning.
- This creates the shortest palindrome by adding characters only at the front.

## Time Complexity
O(n^2), where n is the length of the string.

## Space Complexity
O(n), for storing the remaining suffix and resulting string.

## Edge Case
If the entire string is already a palindrome, no characters need to be added.