s = "abbccccc"

res = ""
count = 1
for i in range(len(s)-1):

    if s[i]==s[i+1]:
        count= count+1

    else:
        res= res+ s[i] + str(count)
        count= 1

res = res+s[len(s)-1] + str(count)

print(res)
    
    