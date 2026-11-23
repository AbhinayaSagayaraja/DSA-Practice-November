# Minimum Changes to Make Alternating Binary String

## Approach
- An alternating binary string can start with either 0 or 1.
- I compare the given string with two possible patterns: 0101... and 1010...
- I count the mismatches for each pattern.
- I return the smaller mismatch count.

## Time Complexity
O(n), where n is the length of the string.

## Space Complexity
O(1), as only two counters are used.

## Edge Case
If the string is already alternating, the minimum number of changes is 0.