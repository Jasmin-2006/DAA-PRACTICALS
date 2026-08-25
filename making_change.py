def making_change(coins, amount):
    # dp[i] represents the minimum number of coins
    # required to make amount i
    dp = [float('inf')] * (amount + 1)

    # Base case
    dp[0] = 0

    # Build the solution from smaller amounts
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount cannot be formed
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


if __name__ == "__main__":
    coins = list(map(int, input("Enter coin denominations: ").split()))
    amount = int(input("Enter amount: "))

    result = making_change(coins, amount)

    if result == -1:
        print("Change cannot be made with the given coins.")
    else:
        print("Minimum number of coins required:", result)
