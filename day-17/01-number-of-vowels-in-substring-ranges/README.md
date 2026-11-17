# Number of Vowels in Substring Ranges

## Approach
Created a prefix sum array to count words that start and end
with vowels. Used prefix sum differences to answer each query.

## Time Complexity
O(n + q)

## Space Complexity
O(n)

## Edge Case
A word containing only one vowel is also counted.