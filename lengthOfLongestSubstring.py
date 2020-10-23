#   Longest Substring Without Repeating Characters
#   Amazon Interview Question

#   ******Sliding Window Apprach******
#   Time complexity : O(2n) = O(n). 
#   In the worst case each character will be visited twice by i and j.

def lengthOfLongestSubstring(s):
    char_set = set()
    n = len(s)
    ans = 0
    i = 0
    j = 0
    while i < n and j < n:
        if(s[j] not in char_set):
            char_set.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            char_set.remove(s[i])
            i += 1
    return ans

s = "abcabcbb"
#s = "bbbbb"
#s = "pwwkew"
print(lengthOfLongestSubstring(s))
