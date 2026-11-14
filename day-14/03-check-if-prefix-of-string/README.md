
# Day 14 - Problem 2: Longest Common Suffix

## Problem Statement

Given an array of strings, find the longest common suffix shared by all strings.

A suffix is a sequence of characters that appears at the end of a string.

If there is no common suffix, return an empty string.

## Examples

**Example 1:**
- Input: ["running", "jogging", "walking"]
- Output: "ing"

**Example 2:**
- Input: ["flower", "power", "tower"]
- Output: "ower"

**Example 3:**
- Input: ["apple", "banana", "orange"]
- Output: ""

## Approach: Reverse Character Comparison

1. Check whether the input list is empty.
2. Take the first string as the reference.
3. Start traversing the first string from its last character.
4. Compare the current character with the corresponding character at the end of every other string.
5. If any character differs or a string is too short, return the suffix found so far.
6. Otherwise, add the matching character to the beginning of the suffix.
7. Continue until the first string is completely checked.

## Complexity Analysis

Let:
- N = Number of strings.
- M = Length of the shortest string.

- Time Complexity: O(N * M).
- Auxiliary Space Complexity: O(1), excluding the output string.

## Key Learning

A common suffix is checked from right to left.

Unlike common prefix matching, we compare characters starting from the end of every string.

## Concepts Used

- Strings
- Arrays
- Nested Loops
- Negative Indexing
- Suffix Matching
