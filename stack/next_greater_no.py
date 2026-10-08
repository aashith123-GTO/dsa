# #brute force approach 
# def next_greater_no(arr):
#     result=[-1]*len(arr)
#     stack=[]
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[j]>arr[i]:
#                 result[i]=arr[j]
#                 print(result)
#                 stack.append(j)
#                 break

#     return result,stack

# print(next_greater_no([3,10,4,2,1,8,11]))


#optimal approach
class Next_Greater_No:
    def __init__(self,arr):
        self.arr=arr
        self.result=[-1]*len(arr)
        self.stack=[]
        
      


    def next_greater_no(self):
        for i in range(len(self.arr)):
            while self.stack and self.arr[i]>self.arr[self.stack[-1]]:
                remove=self.stack.pop()
                self.result[remove]=self.arr[i]

            self.stack.append(i)
            print(self.arr[i])
            print(self.stack,self.result)
        return self.result,self.arr,self.stack
engine = Next_Greater_No([3, 10, 4, 2, 1, 8, 11])
print(engine.next_greater_no())