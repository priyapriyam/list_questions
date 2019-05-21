marks = [[2,4,5,6,],[10,2,6,78,8],[90,5,67,10]]
i=0
sum = 0
total=0
while i<len(marks):
        total=total+sum  
        sum=0
        j=0
        while j < len(marks[i]):
            sum=sum+marks[i][j]
            j=j+1
        print sum
        i=i+1
total=total+sum       
print total

