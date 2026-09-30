
class CicularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*self.size
        self.front=-1
        self.rear=-1
        self.count=0

    def enqueue(self,val):
        if self.count==self.size:
            raise IndexError("Queue OverFlow")

        if self.front==-1 and self.rear==-1:
            self.front=0
            self.rear=0

        self.queue[self.rear]=val
        self.count+=1
        self.rear=(self.rear+1)%self.size
        return self.count,val


    def dequeue(self):
        if self.count==0:
            raise IndexError("Queue UnderFlow")

        remove=self.queue[self.front]
        self.queue[self.front]=None
        self.count-=1

        if self.count==0:
            self.rear=-1
            self.front=-1
        else:
            self.front=(self.front+1)%self.size

        return remove
        
q = CicularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(q.queue)

print(q.dequeue())
print(q.dequeue())

q.enqueue(60)
q.enqueue(70)

print(q.queue)
