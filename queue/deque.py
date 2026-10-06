class Deque:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
        self.count=0

    def insert_rear(self,val):
        if self.count==self.size:
            return "Queue is Full"

        if self.front==-1 and self.rear==-1:
            self.front=0
            self.rear=0


        
        self.queue[self.rear]=val
        self.count+=1
        self.rear=(self.rear+1)%self.size



    def remove_front(self):
        if self.count==0:
            return "Queue is Empty"


        remove=self.queue[self.front]
        self.queue[self.front]=None
        self.count-=1
        if self.count==0:
            self.front=-1
            self.rear=-1
        else:
        
            self.front=(self.front+1)%self.size

        return remove

    def insert_front(self,val):
        if self.count==self.size:
            return "Queue is full"


        if self.front==-1 and self.rear==-1:
            self.front=0
            self.rear=0
        
        self.front=(self.front-1)%self.size
        self.queue[self.front]=val
        self.count+=1
      

    def remove_rear(self):
        if self.count==0:
            return "Queue is empty"

        self.rear=(self.rear-1)%self.size
        remove_rear=self.queue[self.rear]
        self.queue[self.rear]=None
        self.count-=1

        if self.count==0:
            self.front=-1
            self.rear=-1
       
            

        return remove_rear


d = Deque(3)

d.insert_rear(10)
d.insert_rear(20)
d.insert_front(5)

print(d.queue)

print(d.insert_rear(30))
print(d.insert_front(1))

print(d.remove_front())
print(d.remove_rear())