import math

def max_profit_func(prices):
    lowest_buy = math.inf
    max_profit = 0

    for n in prices:
        if n < lowest_buy:
            lowest_buy = n


        curr_profit = n - lowest_buy
        if curr_profit > max_profit:
            max_profit = curr_profit

    return max_profit

print(max_profit_func(prices = [7, 6, 4, 3, 1]))