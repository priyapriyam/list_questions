list=[2,1,7,3,5,4,]
i=0
min_num=list[i]
while i < len(list):
    j=1
    while j < list[i]:
        if min_num > list[j]:
            min_num=list[j]
        else:
            j=j+1
        j=j+1
    i=i+1
print min_num