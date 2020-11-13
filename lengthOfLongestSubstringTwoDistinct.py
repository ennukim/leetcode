#   Longest Substring with At Most Two Distinct Characters
#   Google Interview question
#   *** Sliding Window  ***
#   Time / Space = O(n) / O(n)

def lengthOfLongestSubstringTwoDistinct(s):
    char_d = dict()
    left = 0
    right = 0
    max_length = 2
    if len(s) < 3:
        return len(s)

    while right < len(s):
        #  put in string index for the value
        char_d[s[right]] = right
        right += 1

        if len(char_d) == 3:
            idx = min(char_d.values())
            del char_d[s[idx]]
            left = idx + 1

        max_length = max(max_length, right - left)
    return max_length

# s = "eceba" #3
# s = "ccaabbb" #5
# s = "abc" #2
print(lengthOfLongestSubstringTwoDistinct(s))