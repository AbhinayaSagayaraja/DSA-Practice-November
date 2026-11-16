# Longest Repeating Character Replacement

## Approach
Used a sliding window and a frequency dictionary.
Tracked the maximum character frequency and reduced the window
when the number of replacements required exceeded k.

## Time Complexity
O(n)

## Space Complexity
O(k), where k is the number of distinct characters.

## Edge Case
If k is 0, no characters can be replaced.