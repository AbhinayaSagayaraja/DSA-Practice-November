# Longest Word in Dictionary Through Deleting

## Approach
Used two pointers to check whether each dictionary word
is a subsequence of the given string.
Selected the longest valid word and used lexicographical
comparison when two words had equal length.

## Time Complexity
O(D * (N + K))

D = Number of dictionary words
N = Length of the given string
K = Maximum dictionary word length

## Space Complexity
O(1) auxiliary space.

## Edge Case
If multiple valid words have the same length,
choose the lexicographically smallest word.