# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item in inventory:
    print(f"Processing {item}")
    current_stock = inventory.get(item)[0]
    min = inventory.get(item)[1]
    restock = inventory.get(item)[2]
    sale_status = inventory.get(item)[3]
    while current_stock < min:
        current_stock = current_stock + restock
    if current_stock > discount_threshold:
        sale_status = True
    inventory.get(item)[0] = current_stock
    inventory.get(item)[3] = sale_status

print("Processing completed")