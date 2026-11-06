# Valid Palindrome II

## Approach
Used two pointers to compare characters from both ends.
When a mismatch occurs, checked whether skipping either the
left or right character makes the remaining string a palindrome.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Edge Case
A string that is already a palindrome returns True.