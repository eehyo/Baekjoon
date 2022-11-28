lst=[]
for i in range(9):
    lst.append(int(input()))
print(max(lst))

for i in range(9):
    if lst[i] == max(lst):
        print(i+1)
        break      