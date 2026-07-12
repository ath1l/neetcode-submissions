class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}

        start = 0
        maxim = 0
        for i in range(len(s)): 
            if s[i] in mp:       
                start = max(mp[s[i]] + 1,start)
            mp[s[i]] = i
            maxim = max(maxim,i-start+1)
        return maxim




