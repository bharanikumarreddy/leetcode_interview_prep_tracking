class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start =0
        seen={}
        max_len=0
        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= start :
                start = seen[ch] +1
            seen[ch] = i

        return max_len
