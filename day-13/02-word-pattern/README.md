
# Day 13 - Problem 2: Word Pattern

## Problem Statement

Given a pattern string and a sentence s, determine whether s follows the same pattern.

There must be a one-to-one correspondence between every character in the pattern and every word in the sentence.

Each character must always represent the same word, and each word must represent only one character.

## Examples

**Example 1:**
- Input: pattern = "abba", s = "dog cat cat dog"
- Output: True

**Example 2:**
- Input: pattern = "abba", s = "dog cat cat fish"
- Output: False

**Example 3:**
- Input: pattern = "aaaa", s = "dog cat cat dog"
- Output: False

## Approach: Two Dictionary Mapping

First, split the sentence into individual words using split().

Check whether the number of words matches the length of the pattern.

Create two dictionaries:

1. char_to_word: Maps each pattern character to a word.
2. word_to_char: Maps each word to a pattern character.

Traverse the pattern and words together using an index.

For every character and word:

1. Check whether the character already exists in the first dictionary.
2. If it exists, verify that it maps to the current word.
3. Otherwise, create the mapping.
4. Check whether the word already exists in the reverse dictionary.
5. If it exists, verify that it maps to the current character.
6. Otherwise, create the reverse mapping.

If any mapping conflicts, return False.

If all mappings are consistent, return True.

## Complexity Analysis

- Time Complexity: O(n + m), where n is the pattern length and m is the sentence length.
- Space Complexity: O(n + m), for the words list and dictionaries.

## Key Learning

Word Pattern is similar to Isomorphic Strings.

The difference is that we map characters to complete words instead of mapping characters to characters.

## Concepts Used

- Strings
- String Splitting
- Hash Maps / Dictionaries
- Bidirectional Mapping
