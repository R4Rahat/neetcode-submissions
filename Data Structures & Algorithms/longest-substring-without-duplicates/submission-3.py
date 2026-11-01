class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        i = 0
        res = 0
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]] + 1, i)
            mp[s[j]] = j
            res = max(res, j - i + 1)

        return res