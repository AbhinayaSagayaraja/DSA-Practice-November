# Prefix Scores of Strings

## Approach
Used a trie with nested dictionaries to store the prefixes.
Each node keeps track of how many words contain that prefix.
Traversed each word again and added the prefix counts.

## Time Complexity
O(n * k)

## Space Complexity
O(n * k)

## Edge Case
If words have no common prefixes, each word still gets
a score from its own prefixes.