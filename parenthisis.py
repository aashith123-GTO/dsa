   
#Brute force Approach 
s="{[()]}"
pairs = {"(": ")", "[": "]", "{": "}"}
found=True
while found:
    found=False
    for i in range(len(s)-1):
        if s[i] in pairs and s[i+1]==pairs[s[i]]:
            remove=s[:i]+s[i+2:]
            s=remove
            found=True
            break
            

print(found)
print(s)

if s=="":
    print("Balanced")
else:
    print("Unbalanced")






#Optimal Approach
def parenthesis(s):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}

    for para in s:
        if para in "([{":
            stack.append(para)
        elif para in ")]}":
            if not stack or pairs[stack.pop()]!=para:
                return "Unbalanced"

    return "Balanced" if not stack else "Unbalanced"


print(parenthesis("([])"))   
print(parenthesis("(]"))      
print(parenthesis("((("))  