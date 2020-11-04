import heapq

def minMeetingRooms(intervals):
    if len(intervals) == 0:
        return 0 
    s = sorted(intervals)
    L = [0]
    heapq.heapify(L)
    small = heapq.nsmallest(1, L)
    
    for i in range(len(s)):
        small = heapq.nsmallest(1, L)
        if small[0] > s[i][0]:
            heapq.heappush(L, s[i][1])
        else:
            heapq.heappop(L)
            heapq.heappush(L, s[i][1])
        #print(small)
    return len(L)

# intervals = [[9,10],[4,9],[4,17]] 
# intervals = [[6,15],[13,20],[6,17]]
# intervals = [[7,10],[2,4]] # 1
intervals = []
print(minMeetingRooms(intervals))