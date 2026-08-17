
#brute force approach
def Two_sum_brute(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]
        
    

print(Two_sum_brute([1,2,4,5,6],9))



#optimal approach
def Two_sum_optimal(arr, target):
    two_sum = {}
    for i in range(len(arr)):
        missing_piece = target - arr[i]
        if missing_piece in two_sum:
            return [two_sum[missing_piece], i]
        two_sum[arr[i]] = i

print(Two_sum_optimal([1,2,4,5,6], 9))
    


#two pointer approach
def two_sum_two_ptr(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]+arr[right]==target:
            return [arr[left],arr[right]]
        elif arr[left]+arr[right]<target:
            left+=1
        else:
            right-=1

print(two_sum_two_ptr([1,2,3,4,5,6],9))