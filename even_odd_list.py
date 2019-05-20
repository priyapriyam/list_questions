elements=[23,14,56,12,19,9,15,31,42,43]
i=0
new=[]
new1=[]
while i<len(elements):
    if (elements[i])%2==0:
        new.append(elements[i])
    else:
        new1.append(elements[i])
    i=i+1
print len(new)
print len(new1)
