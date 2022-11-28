N=int(input())
score=list(map(int, input().split()))
new_score=[]
M=max(score)

for i in range(N):
    new_score.append(score[i]/M*100)
    
print(sum(new_score)/N)