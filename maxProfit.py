def maxProfit(prices):
    total_profit = 0 
    peak = 0
    valley = 0
    i = 0

    while (i < len(prices)-1):
        while (i < len(prices)-1 and prices[i] >= prices[i+1]):
            i+=1
        valley = prices[i]

        while (i < len(prices)-1 and prices[i] <= prices[i+1]):
            i+=1
        peak = prices[i]

        total_profit += peak - valley

    return total_profit


def maxProfitV2(prices):
    profit = 0
    for (i, p) in enumerate(prices[:-1]):
        if ((prices[i+1]-p) > 0):
            print(prices[i+1]-p)
            profit += (prices[i+1]-p)
    return (profit)

#this is my version
def maxProfitV3(prices):
    profit = 0
    for i in range(0, len(prices)-1):
        diff = prices[i+1] - prices[i]
        #print(diff)
        if diff > 0:
            profit += diff

    return profit

#prices = [7,1,5,3,6,4]
#prices = [1,0,7,4,8]
#print(maxProfit(prices))
print(maxProfitV3(prices))
