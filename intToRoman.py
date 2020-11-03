def intToRoman(num):
    string = ""
    nums = [1, 4, 5, 9, 10, 40, 50, 90, 
           100, 400, 500, 900, 1000]
    symbol = ["I", "IV", "V", "IX", "X", "XL", 
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    remainder = num

    while remainder:
        quotient = remainder // nums[i]
        remainder %= nums[i]
        while quotient:
            string += symbol[i]
            quotient -= 1
        i-=1

    return string

num = 3549
print(intToRoman(num))