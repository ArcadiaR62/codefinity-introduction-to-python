prices = [29.99, 45.50, 12.75, 38.20]

for index in range(len(prices)):
    if index == 0:
        prices[index] = prices[index] - prices[index]*0.10
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
    elif index == 1:
        prices[index] = prices[index] - prices[index]*0.20
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
    elif index == 2:
        prices[index] = prices[index] - prices[index]*0.15
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
    elif index == 3:
        prices[index] = prices[index] - prices[index]*0.05
        print(f"Updated price for item {index}: ${prices[index]:.2f}")