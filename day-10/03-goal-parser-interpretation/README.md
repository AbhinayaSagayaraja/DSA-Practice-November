# Goal Parser Interpretation

## Approach
Traversed the command string character by character.
Replaced G with G, () with o, and (al) with al.
Built the output using a list and joined it at the end.

## Time Complexity
O(n)

## Space Complexity
O(n)

## Edge Case
An input containing only G should return G.