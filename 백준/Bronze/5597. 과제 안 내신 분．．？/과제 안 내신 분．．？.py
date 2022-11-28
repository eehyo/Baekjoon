student=[]
num=[]
temp=[]

for i in range(1,31):
    student.append(i)
    
for i in range(28):
    num.append(int(input()))


temp=list(set(student)-set(num))     
temp.sort()
print(temp[0])
print(temp[1])