def reorderLogFiles(logs):
    def sorting_algorithm(log):
        left_side, right_side = log.split(" ", 1)

        if right_side[0].isalpha():
            #right side precedes left side
            #once right side is the same, the order is determined by left side
            return (1, right_side, left_side)
       
        else:
            #2 comes after 1 so right side being alpha() precedes the ones that aren't
            #digital right side remains in its ORIGINAL order
            return (2, None, None)

    return sorted(logs, key=sorting_algorithm)


logs = ["dig1 8 1 5 1","let1 art can","dig1 3 6","let2 own kit dig","let3 art zero"]
#logs = ["1 n u", "r 527", "j 527", "6 14", "6 82"]
print(reorderLogFiles(logs))