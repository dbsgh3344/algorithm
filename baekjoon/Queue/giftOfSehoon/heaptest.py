import heapq

a= []
heapq.heapify(a)

for i in [1,5,3,4,7,8]:
    heapq.heappush(a,i)



print(a)
for i in range(len(a)):
    aa= heapq.heappop(a)
    print(aa)