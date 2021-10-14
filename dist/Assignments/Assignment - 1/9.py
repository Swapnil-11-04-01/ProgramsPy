# finding selling price

n = int(input('Enter the number of products : '))
price = int(input('Enter the price of a product : '))
tax = int(input('Enter the tax price : '))
discount = int(input('Enter the discount price : '))

tax_price = (price + (price * float(tax / 100)))
discount_price = tax_price - (tax_price * float(discount / 100))
selling_price = n * discount_price

print(f"Selling Price : {selling_price}")