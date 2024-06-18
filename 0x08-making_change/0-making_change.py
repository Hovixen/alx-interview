#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total
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
