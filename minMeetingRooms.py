import heapq
# My initial approach - doesn't solve.
def minMeetingRooms(intervals):
    s = sorted(intervals)
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
        
    elif len(s) < 3:
        for i in range(len(s)-1):
            if s[i][1] > s[i+1][0]:
                return 2
            else:
                return 1
    else:
        room = 1
        for i in range(len(s)-1):
            if s[i][1] >= s[i+1][0]:
                print("loooo")
                room += 1
            # elif s[i][1] > s[i+1][0] and s[i][1] < s[i+1][1]:
            #     print("effdf")
            #     room += 1
            #     pass
            elif s[i][1] < s[i+1][0] and s[i][1] < s[i+1][1]:
                print("effdf")
                pass
    return room

#intervals = [[0, 30],[5, 10],[15, 20]] # 2
#intervals = [[7,10],[2,4]] # 1
#intervals = [[5,8],[6,8]] # 2
intervals = [[9,10],[4,9],[4,17]] # 2
# intervals = [[6,15],[13,20],[6,17]] #3
# intervals = [[0,30],[5,10],[15,20]] #2
# intervals = [[1,5],[8,9],[8,9]] #2
print(minMeetingRooms(intervals))