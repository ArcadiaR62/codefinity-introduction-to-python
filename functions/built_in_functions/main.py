# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for item in products:
    products.get(item)[0] = float(products.get(item)[0])
    products.get(item)[1] = int(products.get(item)[1])
    total_sales = products.get(item)[0] * products.get(item)[1]
    print(f"Total sales for {item}: ${total_sales}")
    total_sales_list.append(total_sales)

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"Total sum of all sales: ${sum(total_sales_list)}")
print(f"Minimum sales: ${min(total_sales_list)}")
print(f"Maximum sales: ${max(total_sales_list)}")