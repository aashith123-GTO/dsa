def find_duplicate(num):
    copy_cat={}
    for i in range(len(num)):
        if num[i] in copy_cat:
            copy_cat[num[i]]+=1
        else:
            copy_cat[num[i]]=1

    duplicate=[]
    for j in range(len(num)):
        if copy_cat[num[j]]>1 and num[j] not in duplicate:
            duplicate.append(num[j])

    return duplicate



print(find_duplicate([1,1,1,3,4,5,5]))