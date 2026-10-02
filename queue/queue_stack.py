#brute force approach

def queue_using_stack():
    stack1 = []
    stack2 = []

    def enqueue(val):

        while stack1:
            stack2.append(stack1.pop())

        stack1.append(val)

        while stack2:
            stack1.append(stack2.pop())

        print("After enqueue:", stack1)

    def dequeue():
        if not stack1:
            raise IndexError("Queue is Empty")

        return stack1.pop()

    return enqueue, dequeue


enqueue, dequeue = queue_using_stack()

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)

print("Removed:", dequeue())
print("Removed:", dequeue())




#optimal approach
class QueueUsingStack:
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def enqueue(self,val):
        self.stack_in.append(val)
        print(self.stack_in)




    def dequeue(self):
        if not self.stack_in and not self.stack_out:
            return "Queue is Empty"


        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        print("IN:", self.stack_in)
        print("OUT:", self.stack_out)

        return self.stack_out.pop()


q = QueueUsingStack()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())