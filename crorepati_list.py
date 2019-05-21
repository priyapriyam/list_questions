kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
new=[]
new1=[]
new2=[]
while i < len(kitna_paisa_hai):
    if kitna_paisa_hai[i] > 10000000:
        	new.append(kitna_paisa_hai[i])
    elif kitna_paisa_hai[i] > 100000:
        	new1.append(kitna_paisa_hai[i])
    else:
        	new2.append(kitna_paisa_hai[i])
    i=i+1
j=0
while j< len(new):
	j=j+1
print j,"crorepati hai"
k=0
while k<len(new1):
	k=k+1
print k,"lakhpati hai"
l=0
while l<len(new2):
	l=l+1
print l,"Dilwale hai"

        