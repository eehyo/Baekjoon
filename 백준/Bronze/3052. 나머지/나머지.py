num1=[]
num2=[]
for i in range(10):
    num1.append(int(input()))
    
for i in range(10):
    num2.append(num1[i]%42)
    
num2=list(set(num2))

print(len(num2))