
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
    