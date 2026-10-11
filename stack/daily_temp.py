#brute force
temp=[73,45,74,55]
result=[0]*len(temp)
for i in range(len(temp)):
    for j in range(i+1,len(temp)):
        if temp[j]>temp[i]:
            remove=i
            result[remove]=j-remove
            break

print(result)


#optimal approach
class Daily_temp:
    def __init__(self,temp):
        self.temp=temp
        self.result=[0]*len(temp)
        self.stack=[]

    def daily_temperature(self):
        for i in range(len(self.temp)):
            while self.stack and self.temp[self.stack[-1]]<self.temp[i]:
                remove=self.stack.pop()
                self.result[remove]=i-remove

            self.stack.append(i)
        return self.result

dt = Daily_temp([73, 45, 74, 55])
print(dt.daily_temperature())