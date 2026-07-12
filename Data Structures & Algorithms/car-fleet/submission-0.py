class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs  = list(zip(position,speed))
        pairs.sort(reverse=True)
        for i in pairs:
            if not stack:
                time = (target-i[0])/i[1]
                stack.append(time)
            else:
                time = (target-i[0])/i[1]
                if(stack[-1]<time):
                    stack.append(time)
        return len(stack)




