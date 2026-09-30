# Initial approach — single stack
def min_stack(s):
    stack=[]
    current=s[0]
    for i in range(len(s)):
        if s[i]<current:
            current=s[i]
           
        stack.append(current)

    if not stack:
        return False
    else:
        stack.pop()


    removed=stack.pop()
    if removed>=current:
        current=removed



    return current

print(min_stack([2,1,3,4]))





#optimal approach
class minstack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
    def push(self,val):
            self.stack.append(val)
            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])


    def pop(self):
        if self.stack and self.min_stack:
            self.min_stack.pop()
            self.stack.pop()
    

    def Top(self):
        return self.stack[-1]

    def getmin(self):
        if not self.min_stack:
            return False
        return self.min_stack[-1]


ms = minstack()

ms.push(2)
ms.push(1)
ms.push(3)
ms.push(4)

print(ms.stack)
print(ms.min_stack)

print(ms.Top())
print(ms.getmin())

ms.pop()
ms.pop()
ms.pop()
print(ms.stack)
print(ms.min_stack)

print(ms.Top())
print(ms.getmin())


    

            