def Last_in_first_out(size):
    stack=[]
    count=0

    def push(val):
        nonlocal stack,count
        if count==size:
            raise OverflowError( 'Stack OverFlow')
        stack.append(val)
        count+=1
        return val,count


    def pop():
        nonlocal stack,count
        if count==0:
            raise IndexError("Stack Underflow")
        top=stack.pop()
        count-=1
        return top,count

    def peek():
        if count==0:
            raise   IndexError( "Stack is Empty")
        return stack[-1]


    def isEmpty():
        return count==0



    return push,pop,peek,isEmpty


push, pop, peek, isEmpty = Last_in_first_out(4)

print(isEmpty())
print("Push->", push(4))
print("Push->", push(5))
print("Push->", push(7))
print("Push->", push(8))

try:
    push(1)
except OverflowError as e:
    print("Push->", e)

print("Pop->", pop())
print("Peek", peek())
print("Pop->", pop())
print("Peek->", peek())
print("Pop->", pop())
print("Pop->", pop())

try:
    pop()
except IndexError as e:
    print("Pop->", e)

try:
    peek()
except IndexError as e:
    print("Peek->", e)
