sort =[4,2,3,1,6,8]
a=0
b=len(sort)
new=[]
while a < b:
    i=min(sort)
    new.append(i)
    sort.remove(i)
    a=a+1
print new