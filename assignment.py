# Question 1
def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

print(calculate_discount(100, 20))
print(calculate_discount(100, 25))

print("\n")

# Question 2
def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price
    
price = int(input("Enter price: "))
discount_percent = int(input("Enter discount percentage: "))
    
print(calculate_discount(price, discount_percent))