a="2018A4PS0510G"
sum=0
for i in range(len(a)):
	if a[i].isdigit():
		sum = sum + int(a[i])
print(sum)
