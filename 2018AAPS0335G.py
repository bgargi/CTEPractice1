b=[2,0,1,8,'a','a','p','s',0,3,3,5,'g']
count=0
for i in range(len(b)-1):
	if type(b[i])==int:
		count=count+b[i]

print(count)
