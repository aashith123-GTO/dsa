def ischeck_pair_exist(num,target):
    seen={}
    for i in range(len(num)):
        needed=target-num[i]
        if needed  in seen:
            return True
        seen[num[i]]=i

    return False



print(ischeck_pair_exist([10,15,3,7],17))