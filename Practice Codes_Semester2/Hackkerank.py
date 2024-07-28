n=5
cost=[2,5,3,11,1]
labels=['legal','illegal','legal','illegal','legal']
dailyCount=2
l1=[]
d={}
for i in range(len(cost)):
    for j in range(len(labels)):
        if i==j:
            d[cost[i]]=labels[j]
print(d)
count_legal=0
cost=0


    


