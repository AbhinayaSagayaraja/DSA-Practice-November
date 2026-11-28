# Check If a Word Occurs As Prefix of Any Word

## Approach
- I traverse the sentence and build each word character by character.
- I compare the beginning of each word with the searchWord.
- If a match is found, I return that word's 1-based position.
- If no word matches, I return -1.

## Time Complexity
O(n + m), where n is the sentence length and m is the searchWord length.

## Space Complexity
O(n), for storing the current word.

## Edge Case
If the searchWord is longer than every word, return -1.