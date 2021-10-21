a = [1,3,5,12]
b = []
n = len(a)
m = len(b)

c = []
i = 0 #a
j = 0 #b
k = 0
while(i < n  and j < m):
    if(a[i] > b[j]):
        c.append(b[j])
        # c[k] = b[j]
        # k += 1
        j += 1
    else: 
        c.append(a[i])
        i += 1
while(i < n):
    c.append(a[i])
    i += 1
while(j < m):
    c.append(b[j])
    j += 1

print(c)