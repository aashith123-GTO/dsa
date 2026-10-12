#brute force
def next_greater_ele_2(arr):
    n = len(arr)
    result = [-1] * n
    for i in range(n):
        for j in range(1,n):
            j=(i+j)%n
            if arr[j]>arr[i]:
                remove=i
                result[remove]=arr[j]
                break
    return result

print(next_greater_ele_2([1,5,2,4]))



#optimal approach
def next_greater_ele_2(arr):
    n=len(arr)
    result=[-1]*n
    stack=[]
  
    for i in range(2*n):
        index=i%n
        while stack and arr[index]>arr[stack[-1]]:
            remove=stack.pop()
            result[remove]=arr[index]
        
        
        stack.append(index)
    return result,stack
print(next_greater_ele_2([1, 5, 2, 4]))


