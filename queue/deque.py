def deque_shifting_method(size):
    arr=[None]*size
    count=0

    def push_front(val):
        nonlocal count
        if count==size:
            return "Queue is Full"
        for i in range(count-1,-1,-1):
            arr[i+1]=arr[i]

        arr[0]=val
        count+=1

    def push_rear(val):
        nonlocal count   
        if count==size:
            return "Queue is Full"

        arr[count]=val
        count+=1

    def pop_front():
        nonlocal count
        if count==0:
            return "Queue is Empty"

        value=arr[0]
        for i in range(0,count-1):
            arr[i]=arr[i+1]

        arr[count-1]=None
        count-=1

        return value

    def pop_rear():
        nonlocal count
        if count==0:
            return "Queue is Empty"

        value=arr[count-1]
        arr[count-1]=None
        count-=1
        return value
    return push_front, push_rear, pop_front, pop_rear,arr

push_front, push_rear, pop_front, pop_rear,arr = deque_shifting_method(3)

push_front(10)
print(arr)
push_front(30)
print(arr)
push_front(40)
print(arr)
push_front(30)
print(arr)

print(pop_front())
push_front(2)
print(arr)
print(pop_rear())
push_rear(40)
print(arr)

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
       
            

        return remove_rear,self.queue


d = Deque(3)

d.insert_rear(10)
print(d.queue)
d.insert_rear(20)
print(d.queue)
d.insert_front(5)
print(d.queue)


print(d.insert_rear(30))
print(d.queue)
print(d.insert_front(1))
print(d.queue)

print(d.remove_front())
print(d.queue)
print(d.remove_rear())
print(d.queue)