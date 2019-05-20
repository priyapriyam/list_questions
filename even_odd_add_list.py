elements=[23,14,56,12,19,9,15,31,42,43]
i=0
new=[]
new1=[]
sum=0
sum1=0
while i<len(elements):
    if (elements[i])%2==0:
        new.append(elements[i])
        sum=sum+(elements[i])
    else:
        new1.append(elements[i])
        sum1=sum1+(elements[i])    
    i=i+1
print len(new)
print len(new1)
print sum
print sum1