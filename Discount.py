def get_discounted_price(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price

price = float(input("Enter the price: "))
discount = float(input("Enter the discount percentage: "))
final_price = get_discounted_price(price, discount)

print("Final price:", final_price)
