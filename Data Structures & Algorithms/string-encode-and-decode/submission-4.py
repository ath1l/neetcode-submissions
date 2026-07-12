class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result = result + str(len(word)) + "#" + word
            print(result)
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i,j = 0,0 
        while i<len(s):
            while(s[j] != '#'):
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = j + length + 1
            result.append(s[i:j])
            i = j
        return result