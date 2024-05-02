#!/usr/bin/python3
"""This function calculates the minimum number of coins required
   to reach a given total."""

def makeChange(coins, total):
    """Calculates the minimum number of coins required
       to reach a given total amount."""
    if total <= 0:
        return 0

    current_total = 0
    used_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - current_total) // coin
        current_total += r * coin
        used_coins += r
        if current_total == total:
            return used_coins
    return -1
