def print_catalog(catalog):
    for item in catalog:
        print(f"Item: {item['name']}, Price: ${item['price']}")

# Example usage
catalog = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Smartphone', 'price': 800},
    {'name': 'Tablet', 'price': 400}
]

print_catalog(catalog)
