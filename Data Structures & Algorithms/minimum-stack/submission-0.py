class MinStack:

    def __init__(self):
        self.s=[]
        self.m=[]

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.m:
            self.m.append(val)
        elif self.m[-1] >= val:
            self.m.append(val)



    def pop(self) -> None:
        if(self.s[-1] == self.m[-1]):
            self.s.pop()
            self.m.pop()
        else:
            self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
        
