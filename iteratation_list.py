mentors =["Pratyush","Diwakar","Rahul","divya","Ankita"]
mentees =[6,7,8,4,5]

print len(mentors)
print len(mentees)

length = len(mentors)
count=0
while count < length:
	print mentors[count]+str(mentees[count])
	count=count+1
