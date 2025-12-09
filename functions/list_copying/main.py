# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

#Difine the function
def apply_discount(prices):
    prices_copy = prices.copy()
    for index in range(len(prices_copy)):
        if prices_copy[index] > 2.00:
            prices_copy[index] = prices_copy[index] * (1 - 0.1)

    return prices_copy

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

# Print final result
print(f"Updated product prices: {updated_prices}")