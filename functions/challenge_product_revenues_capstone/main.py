# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for index in range(len(prices)):
        revenue.append(prices[index] * quantities_sold[index])
    return revenue

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = zip(products, revenue)

def formatted_output(revenues):
    revenues = sorted(revenues)
    for products, revenue in revenues:
        print(f"{products} has total revenue of ${revenue}")
    return revenues


    
revenue_per_product = formatted_output(revenue_per_product)
# Example of expected output line (do not remove):
print(f"{revenue[0]} has total revenue of ${revenue[1]}")