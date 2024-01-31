#Data

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]



# Calculate the total price average for all products

average_price = sum(prices) / len(prices)

print(f"Average Price: ${average_price:.2f}")



# Create a new price list that reduces the old prices by $5

new_prices = [price - 5 for price in prices]

print("New Prices:", new_prices)



# Calculate the total revenue generated from the products

total_revenue = sum(price * quantity for price, quantity in zip(prices, last_week))

print(f"Total Revenue: ${total_revenue:.2f}")



# Calculate the average daily revenue generated from the products

average_daily_revenue = total_revenue / len(last_week)

print(f"Average Daily Revenue: ${average_daily_revenue:.2f}")



# Find the product with the highest revenue

max_revenue_index = last_week.index(max(last_week))

max_revenue_product = products[max_revenue_index]

print(f"Product with the highest revenue: {max_revenue_product}")



# Find the product with the lowest revenue

min_revenue_index = last_week.index(min(last_week))

min_revenue_product = products[min_revenue_index]

print(f"Product with the lowest revenue: {min_revenue_product}")



# Identify products with prices less than $30 based on the new prices

affordable_products = [product for product, price in zip(products, new_prices) if price < 30]

print("Products with Price < $30:", affordable_products)
