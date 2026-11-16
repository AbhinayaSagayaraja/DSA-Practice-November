def lenOfLongestSubstring(s):
    freq = {}
    left = 0
    longest = 0
    for right in range(len(s)):
        ch = s[right]
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
        while freq[ch] > 1:
            freq[s[left]] -= 1
            left += 1
        size = right - left + 1
        if size > longest:
            longest = size
    return longest
s = "abcabcbb"
print(lenOfLongestSubstring(s))