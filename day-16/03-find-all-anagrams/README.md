# Find All Anagrams in a String

## Approach
Created frequency dictionaries for the pattern and the first window.
Slid the window one character at a time by adding the new character
and removing the character leaving the window.

## Time Complexity
O(n * k), where k is the number of distinct characters.

## Space Complexity
O(k), where k is the number of distinct characters.

## Edge Case
If the pattern is longer than the string, return an empty list.