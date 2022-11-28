C=int(input())

for i in range(C):
    avg = 0
    num = list(map(int, input().split()))
    N=num[0]
    score = num[1:]
    avg = sum(score)/N
    M=0
        
    for j in score:
        if j > avg:
            M += 1
    per=M/N*100
    print(f'{per:.3f}%')