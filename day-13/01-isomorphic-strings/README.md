
# Day 13 - Problem 1: Isomorphic Strings

## Problem Statement

Given two strings s and t, determine whether they are isomorphic.

Two strings are isomorphic if characters in the first string can be replaced to obtain the second string.

Each character must map consistently to exactly one character. Two different characters cannot map to the same character.

## Examples

**Example 1:**
- Input: s = "egg", t = "add"
- Output: True

**Example 2:**
- Input: s = "foo", t = "bar"
- Output: False

**Example 3:**
- Input: s = "paper", t = "title"
- Output: True

## Approach: Two Dictionary Mapping

We create two dictionaries:

1. s_to_t: Maps characters from string s to string t.
2. t_to_s: Maps characters from string t to string s.

We traverse both strings using an index.

For every pair of characters:

1. Check whether the first character already has a mapping.
2. If it exists, verify that it maps to the current second character.
3. Otherwise, create the mapping.
4. Perform the same check in the reverse direction.
5. If either mapping is inconsistent, return False.

If all characters satisfy both mappings, return True.

## Complexity Analysis

- Time Complexity: O(n), where n is the length of the strings.
- Space Complexity: O(n), for the two dictionaries.

## Key Learning

Isomorphic strings require a bidirectional one-to-one mapping.

Both dictionaries are necessary to prevent multiple characters from mapping to the same character.

## Concepts Used

- Strings
- Hash Maps / Dictionaries
- Character Mapping
- One-to-One Mapping
