def romanToInt(s):
    symbol = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    num = 0
    i = 0

    while i < len(s):
        if s[i:i+2] in symbol:
            num += symbol[s[i:i+2]]
            i+=2
        else:
            num += symbol[s[i]]
            i+=1
    return num

# alternate answer which uses (+ - + -) method as it traverses the input string
# much efficient
def romanToInt2(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]

s = "MCMXCIV"
print(romanToInt2(s))