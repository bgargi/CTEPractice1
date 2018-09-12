a=[2,0,1,8,"A",4,"P","S",0,5,1,4,"G"]
count=0
for i in range(len(a)-1):
	if type(a[i])==int:
	count=count+a[i]

print(count)
