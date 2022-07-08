

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
flights = [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]

#src = 0
#dst = 3
#k = 1

src = 0
dst = 4
k = 1
import pdb;pdb.set_trace()
total_price = 0
for flight in flights:
    if flight[0] == src:
        if flight[1] == k or flight[1] == dst:
            total_price += flight[2]
            src = flight[1]

if total_price == 0:
    print(-1)
else:
    print(total_price)


