#this one isn't a leetcode problem but it's widely known

def second_smallest(lst):
    first = lst[0]
    second = lst[0]

    for i in range(len(lst)):
        if lst[i] < first:
            second = first
            first = lst[i]
        elif lst[i] < second and lst[i] != first:
            second = lst[i]
        
    return second



lst = [12, 13, 1, 10, 34, 1]
print(second_smallest(lst))