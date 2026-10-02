class StackUsingQueue:
    def __init__(self):
        self.queue=[]
        self.queue2=[]
       
    def enqueue(self,val):
        self.queue.append(val)


    def dequeue(self):
        if not self.queue and not self.queue2:
            return "Stack is Empty"

        if not self.queue2:
            while self.queue:
                self.queue2.append(self.queue.pop(0))
        
        return self.queue2.pop()
  


suq=StackUsingQueue()
suq.enqueue(10)
suq.enqueue(20)
suq.enqueue(30)
suq.enqueue(40)
print(suq.dequeue())



from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.queue1=deque()
        self.queue2=deque()

    def push(self,val):
        self.queue2.append(val)
       
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self):
        if not self.queue1:
            return "Stack is Empty"

        return self.queue1.popleft()

suq=StackUsingQueue()
suq.push(10)
suq.push(20)
suq.push(30)
suq.push(40)
print(suq.pop())
print(suq.pop())
