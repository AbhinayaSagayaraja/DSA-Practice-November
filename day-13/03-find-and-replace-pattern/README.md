
# Day 13 - Problem 3: Find and Replace Pattern

## Problem Statement

Given a list of words and a pattern, find all words that match the given pattern.

A word matches the pattern if there is a one-to-one mapping between its characters and the characters in the pattern.

The mapping must remain consistent throughout the word.

Return all matching words in the original order.

## Examples

**Example 1:**
- Input: words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
- Pattern: "abb"
- Output: ["mee", "aqq"]

**Example 2:**
- Input: words = ["a", "b", "c"]
- Pattern: "a"
- Output: ["a", "b", "c"]

## Approach: Two Dictionary Mapping

We iterate through every word in the given list.

For each word:

1. Check whether its length matches the pattern length.
2. Create two empty dictionaries:
   - word_to_pattern: Maps characters from the current word to pattern characters.
   - pattern_to_word: Maps pattern characters to word characters.
3. Traverse both strings using an index.
4. Check whether an existing mapping is consistent.
5. If a mapping does not match, mark the word as invalid and stop checking it.
6. If both mappings remain consistent, add the word to the result list.

Finally, return the result list.

## Complexity Analysis

Let:
- N = Number of words.
- K = Maximum length of a word.

- Time Complexity: O(N * K).
- Auxiliary Space Complexity: O(K) for the two dictionaries used to check one word at a time.
- Output Space: O(N * K) in the worst case for the result list.

## Key Learning

This problem applies the same bidirectional mapping technique used in Isomorphic Strings.

Instead of checking only one pair of strings, we apply the mapping logic to every word in a list.

## Concepts Used

- Strings
- Lists
- Hash Maps / Dictionaries
- Bidirectional Mapping
- Pattern Matching
