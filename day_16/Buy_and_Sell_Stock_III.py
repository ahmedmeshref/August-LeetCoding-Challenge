import sys
from collections import deque


def maxProfit(prices) -> int:
    profits_1 = [0]
    min_price = sys.maxsize
    for price in prices:
        min_price = min(min_price, price)
        profits_1.append(max(profits_1[-1], price - min_price))

    profits_2 = deque()
    profits_2.append(0)
    max_price = 0
    for i in range(len(prices)-1, -1, -1):
        max_price = max(max_price, prices[i])
        profits_2.appendleft(max(profits_2[0], max_price - prices[i]))

    max_profit = 0
    for i in range(len(profits_1)):
        max_profit = max(max_profit, profits_1[i] + profits_2[i])
    return max_profit


print(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
