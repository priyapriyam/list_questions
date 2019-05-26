number=[19,21,15,20,1,4,18,3,7,10,122,13]
a=0
while a<len(number):
    b=a+1
    while b<len(number):
        if number[a] > number[b]:
            c=number[a]
            number[a]=number[b]
            number[b]=c
        b=b+1
    a=a+1

    
