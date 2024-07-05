#!/usr/bin/python3
"""
A prime game
"""


def isWinner(x, nums):
    """ The prime game function """
    def sieve_of_eratosthenes(max_n):
        """ Create a boolean array "prime[0:max_n]" and initialize all
        entries it as true

        A value in prime[i] will finally be false if i is
        Not a prime, else true."""

        prime = [True for _ in range(max_n + 1)]
        p = 2
        while (p * p <= max_n):
            # If prime[p] is not changed, then it is a prime
            if prime[p] is True:
                # Updating all multiples of p to not prime
                for i in range(p * p, max_n + 1, p):
                    prime[i] = False
            p += 1
        # Collect all prime numbers
        return [p for p in range(2, max_n + 1) if prime[p]]

    def simulate_game(n):
        if n == 1:
            return "Ben"
        primes = sieve_of_eratosthenes(n)
        remaining = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        while primes:
            # Select the smallest available prime (optimal strategy)
            current_prime = primes.pop(0)
            # Remove the prime and its multiples from the remaining set
            for multiple in range(current_prime, n + 1, current_prime):
                if multiple in remaining:
                    remaining.remove(multiple)
            # Recompute primes based on remaining numbers
            primes = [p for p in primes if p in remaining]
            # Switch turns
            turn = 1 - turn
        # The last turn was made by the losing player, return the winner
        return "Ben" if turn == 0 else "Maria"

    # Track wins for both players
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins +=1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
