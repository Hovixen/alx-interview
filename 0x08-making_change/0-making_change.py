#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Minium coins required
    """
    if total <= 0:
        return 0
    trace, count = 0, 0
    coins.sort()
    coins = coins[::-1]
    while len(coins) > 0:
        value = coins[0]
        if trace + value > total:
            coins.pop(0)
            continue
        trace += value
        count += 1
        if trace == total:
            return count
    return -1


"""
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with infinity for all values except dp[0]
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make 0 amount

    # Fill dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if it's possible to form the total
    return dp[total] if dp[total] != float('inf') else -1
"""
