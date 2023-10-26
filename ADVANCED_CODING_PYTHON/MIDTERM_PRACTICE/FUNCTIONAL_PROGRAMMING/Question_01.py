"""Write a function that applies a discount to a price and another that applies VAT to a price. Write a third function 
that receives a dictionary with the prices and percentages of a shopping cart, and one of the previous functions, and 
uses the last function to apply the discounts or VAT to the products in the cart and return the final price of the cart."""

def discount(price, discount_percentage):
    discount = price * (discount_percentage / 100)
    discounted_price = price - discount
    return discounted_price

def apply_vat(price, vat_percentage):
    vat_amount = price * (vat_percentage / 100)
    price_with_vat = price + vat_amount
    return price_with_vat

def process_shopping_cart(cart, function):
    
    total = 0    
    for price, discount in cart.items():
        total += function(price, discount)
    return total

shopping_cart_discount = {
    5:5,
    10:3,
    70:20 
}

shopping_cart_vat = {
    5:40,
    10:100,
    70:20 
}

price_discount = process_shopping_cart(shopping_cart_discount, discount)
price_vat = process_shopping_cart(shopping_cart_vat, apply_vat)

print('Total Price With Discount: ',price_discount)
print('Total Price With VAT: ', price_vat)