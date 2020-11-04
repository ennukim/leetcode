#   Sorting method
def canAttendMeetings2(intervals):
    if len(intervals) <= 1:
            return True
    s = sorted(intervals)
    for i in range(len(s)-1):
        if s[i][1] > s[i+1][0]:
            return False
    return True 

#   My initial approach w/ bruteforce
#   Time complexity - O(n^2)
def canAttendMeetings(intervals):
    i = 0
    p = 0
    while p < len(intervals)-1:
        for k in range(len(intervals)-1):
            if intervals[p] == intervals[k+1] and p != k+1:
                print(intervals[p], intervals[k+1])
                return False
            else:
                pass
        p += 1

    while i < len(intervals)-1:
        #print("hello")
        for j in range(len(intervals)-1):
            if intervals[i][0] == intervals[j+1][0] and intervals[i][1] == intervals[j+1][1]:
                pass
            elif intervals[i][0] < intervals[j+1][0]:
                #print("hello")
                if intervals[i][1] > intervals[j+1][0]:
                    return False
                else:
                    pass
            else:
                if intervals[i][0] < intervals[j+1][1]:
                    return False
                else:
                    pass
        i += 1
    return True

#intervals = [[7,10],[2,4]] # True
#intervals = [[15,16],[10,15],[16,25]] # True
#intervals = [[8,11],[17,20],[17,20]] # True
#intervals = [[0,30],[5,10],[15,20]] # False
intervals = [[0,30],[60,240],[90,120]]
print(canAttendMeetings2(intervals))