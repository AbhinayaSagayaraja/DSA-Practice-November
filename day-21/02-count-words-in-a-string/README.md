# Count Words in a String

## Approach
- I traverse the string character by character.
- I use a boolean variable to check whether I am inside a word.
- Whenever a new word starts, I increase the count.

## Time Complexity
O(n), where n is the length of the string.

## Space Complexity
O(1), as only two variables are used.

## Edge Case
Multiple spaces between words should not be counted as separate words.