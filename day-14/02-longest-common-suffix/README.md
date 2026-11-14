
# Day 14 - Problem 1: Longest Common Prefix

## Problem Statement

Given an array of strings, find the longest common prefix shared by all strings.

If there is no common prefix, return an empty string.

## Examples

**Example 1:**
- Input: ["flower", "flow", "flight"]
- Output: "fl"

**Example 2:**
- Input: ["dog", "racecar", "car"]
- Output: ""

**Example 3:**
- Input: ["apple", "application", "apply"]
- Output: "appl"

## Approach: Character-by-Character Comparison

1. Check whether the input list is empty.
2. Take the first string as the reference.
3. Traverse each character of the first string.
4. Compare that character with the same position in every other string.
5. If a string is shorter or the character does not match, return the prefix found so far.
6. Otherwise, add the character to the prefix.
7. Return the final prefix.

## Complexity Analysis

Let:
- N = Number of strings.
- M = Length of the shortest string.

- Time Complexity: O(N * M).
- Auxiliary Space Complexity: O(1), excluding the output string.

## Key Learning

A common prefix must have the same characters at the same positions in every string.

We can find it by manually comparing characters using nested loops.

## Concepts Used

- Strings
- Arrays
- Nested Loops
- Character Comparison
- Prefix Matching
