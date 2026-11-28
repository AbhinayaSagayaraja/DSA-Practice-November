# Longest Word With All Prefixes Present

## Approach
- I store all words in a set for quick lookup.
- For every word, I check whether all its prefixes are present.
- Among valid words, I select the longest one.
- If lengths are equal, I select the lexicographically smaller word.

## Time Complexity
O(n * L^2), where n is the number of words and L is the maximum word length.

## Space Complexity
O(n * L), for storing the words in a set.

## Edge Case
If no word has all its prefixes present, return an empty string.