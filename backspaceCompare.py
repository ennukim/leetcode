# Backspace String Compare
# Google interview - Arrays & Strings

def backspaceCompare(S, T):
    count = 0
    ns = ""
    nt = ""
    for i in range(len(S)-1,-1,-1):
        if S[i] == "#":
            count += 1
        elif S[i].isalpha() and not count:
            ns += S[i]
        elif S[i].isalpha():
            count -= 1
    count = 0
    for i in range(len(T)-1,-1,-1):
        if T[i] == "#":
            count += 1
        elif T[i].isalpha() and not count:
                nt += T[i]
        elif T[i].isalpha():
            count -= 1
        
    # print(ns, nt)
    return ns == nt

# True
# S = "ab#c"
# T = "ad#c"
# S = "a##c"
# T = "#a#c"
# S = "ab##"
# T = "c#d#"

# False
S = "a#c"
T = "b"
print(backspaceCompare(S, T))
