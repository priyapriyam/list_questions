list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=0
new =[]
while i < len(list):
	if i % 2 == 0:
		new.append(list[i])
	i=i+1
print new 
