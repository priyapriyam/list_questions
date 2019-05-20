elements=[23,14,56,12,19,9,15,31,42,43]
i=0
new=[]
new1=[]
total=0
sum1=0
sum2=0
while i<len(elements):
    total=total + elements[i]
    	if (elements[i])%2==0:#to find out even numbers
        new.append(elements[i])
        sum1=sum1+(elements[i])
    else:
        new1.append(elements[i])# to find out odd numbers
        sum2=sum2+(elements[i])
    i=i+1
print len(elements)#length of list(10)
print len(new)#length of even number list(4)
print len(new1)# lenght of odd number list(6)
print (total)	#sum of list(264)
print (sum1)	#sum of even list(124)
print (sum2) 	#sumof odd list(140)
avg_total=264/10 #avg of list(26)
print avg_total	
avg_even=124/4	#avg of even list(31)
print avg_even
avg_odd=140/6	#avg of odd list(23)
print avg_odd





