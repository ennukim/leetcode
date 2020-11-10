# Amazon Interview Ques

def merge(intervals):
    if len(intervals) == 0:
        return []
    intervals = sorted(intervals)
    lst = []
    lst.append(intervals[0])
    for interval in intervals[1:]:
        if interval[0] <= lst[-1][1]:
            lst[-1][1] = max(lst[-1][1], interval[1])
        else:
            lst.append(interval)
    return lst

#My Version 
#Intercetions more than 2 doesn't work with this algorithm
def merge1(intervals):
    lst = []
    count = 0
    flag = False
    if len(intervals) <= 1:
        return intervals
    new_inter = sorted(intervals)
    first = new_inter[0][0]
    second = new_inter[0][1]

    for i in range(1, len(new_inter)):
        if second >= new_inter[i][0] and second < new_inter[i][1]:
            second = new_inter[i][1]
            flag = True

        elif second >= new_inter[i][0] and second >= new_inter[i][1]:
            pass
        else:
            if not flag:
                lst.append([first, second])
            first = new_inter[i][0]
            second = new_inter[i][1]
        
        lst.append([first, second])
           
    return lst

intervals = [[1,3],[2,6],[6,10],[10,18]]
# intervals = [[1,4],[5,6],[6,7]]
# intervals = [[1,4],[2,3]]
# intervals = [[1,4],[0,2],[3,5]]
print(merge(intervals))
