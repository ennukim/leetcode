import math
import heapq

def kClosest(points, K):
    min_dist = float('inf')
    h = []

    if len(points) == K:
        return points

    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        dist = math.sqrt(pow(x,2) + pow(y,2))
        heapq.heappush(h, [dist, [x,y]])

    ans = heapq.nsmallest(K, h)

    return [i[1] for i in ans] 

points = [[1,3],[-2,2],[2,-2]]
K = 2
print(kClosest(points, K))