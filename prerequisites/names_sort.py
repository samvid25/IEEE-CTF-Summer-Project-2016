names=[]
for i in range (0,10):
	name=raw_input()
	names.append(name)


for i in range (0,len(names)-1):
	for j in range (0,len(names)-i-1):
		if(names[j]>names[j+1]):
			names[j],names[j+1]=names[j+1],names[j]
print names
