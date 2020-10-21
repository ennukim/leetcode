#leetcode common answer
def licenseKeyFormatting2(S, K):
    S = S.replace("-", "").upper()[::-1]
    return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]

#My version at first_try
def licenseKeyFormatting(S, K):
    S = S.replace("-", "")
    new_string = ""
    count = 0
    length = len(S)
    rem = int(length % K)

    if rem == 0:
        #print("Even")
        while count < length:
            for i in range(K):
                new_string += S[count]
                count += 1
            new_string += '-'
    else:
        for i in range(rem):
            new_string += S[i]
            count += 1
        new_string += '-'
        while count < length:
            for j in range(K):
                new_string += S[count]
                count += 1
            new_string += '-'
    return new_string[:-1].upper()

# S = "5F3Z-2e-9-w"
# K = 4
# S = "2-5g-3-J"
# K = 2
S = "2-4A0r7-4k"
K = 3
print(licenseKeyFormatting2(S, K))