def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent /100)
        return discounted_price
    else:
        return price
    
    #Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
original_price = float(input("Please enter the original price of the item you want to purchase?"))
discount_percentage = float(input("please enter the discount percentage of the item you want to purchase?"))
    
    #calculating for the final price after the discount as been applied.
final_price = calculate_discount(original_price, discount_percentage)

#Printing Final price.
print("Final price after the discount: ${:.2f}".format(final_price))
    
    
def outer_fun(a, b):
        def inner_fun(c, d):
            return c + d
        return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

for num in range(1, 5):
    print(num)

x = 0
for i in range(3):
    x = x + i