a="2018A7PS0167G"
sum=0
for i in range(len(a)):
    if a[i].isdigit():
        sum = sum + int(a[i])
print(sum)
