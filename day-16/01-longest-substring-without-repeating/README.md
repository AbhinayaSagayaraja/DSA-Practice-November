# Longest Substring Without Repeating Characters

## Approach
Used a sliding window with two pointers and a frequency dictionary.
Expanded the window and moved the left pointer whenever a character repeated.

## Time Complexity
O(n)

## Space Complexity
O(k), where k is the number of distinct characters.

## Edge Case
An empty string returns 0.