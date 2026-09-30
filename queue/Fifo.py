class fifo:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
        self.count=0

    def enqueue(self,val):
        if self.count==self.size:
            raise IndexError("Queue Full")

        if self.front==-1 and self.rear==-1:
            self.front=0
            self.rear=0
        


        self.queue[self.rear]=val
        self.rear+=1
        self.count+=1

        return val

    def dequeue(self):
        remove=self.queue[self.front]
        self.queue[self.front]=None
        self.front+=1
        self.count-=1
        if self.count==0:
            self.front=-1
            self.rear=-1
            
        

        return remove



q = fifo(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(q.queue)

q.dequeue()
q.dequeue()

print(q.queue)
print(q.front, q.rear, q.count)

q.enqueue(60)
       
