class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        count = 0
        left = 0
        res = 0
        for i in range(len(s)):
            if s[i] in mp and mp[s[i]] >= left:
                left = mp[s[i]] + 1
                res = max(res,i-left+1)
                mp[s[i]] = i
            else:
                mp[s[i]] = i
                res = max(res,i-left+1)

        return res

