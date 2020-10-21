def isPalindrome(s):
    if s == "":
        return True

    i = 0
    j = len(s)-1
    left = s[i]
    right = s[j]

    while (i<j):
        left = s[i]
        right = s[j]

        while not left.isalnum() and (i<j):
            i+=1
            left = s[i]
        while not right.isalnum() and (i<j):
            j-=1
            right = s[j]

        if left.isupper():
            left = left.lower()
        if right.isupper():
            right = right.lower()
        if (left == right):
            i+=1
            j-=1
        if (left != right):
            return False

    return True

def isPalindrome2(s):
    cleared = [i for i in s.lower() if i.isalnum()]
    return cleared[::-1] == cleared

#s = "A man, a plan, a canal: Panama"
s = "race a car"
print(isPalindrome2(s))
