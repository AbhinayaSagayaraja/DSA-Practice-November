# Longest Palindrome

## Approach
Counted the frequency of every character using a dictionary.
Used all even frequencies and one character from an odd
frequency to calculate the maximum palindrome length.

## Time Complexity
O(n)

## Space Complexity
O(k), where k is the number of distinct characters.

## Edge Case
If all characters are different, the maximum palindrome length is 1.