class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        k=len(s)-1
        while i<k:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[k].isalnum():
                k-=1
                continue

            if s[i].lower() == s[k].lower():
                i+=1
                k-=1
            else:
                return False
        return True            
            

                

