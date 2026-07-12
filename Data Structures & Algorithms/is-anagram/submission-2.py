class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countT = {}
        countS = {}

        for ch in s:
            countT[ch] = countT.get(ch,0) + 1

        for ch in t:
            countS[ch] = countS.get(ch,0) + 1

        if(countS == countT):
            return True
        
        return False