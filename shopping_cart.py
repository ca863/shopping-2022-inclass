# shopping_cart.py

print("When all products are scanned please type 'DONE'")

from ast import For, NotIn


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# CHECKPOINT 1: CAPTURING USER INPUTS
total_price = 0
selected_ids = []
possible_identifiers = []

for x in products:
    if x["id"] not in possible_identifiers:
        possible_identifiers.append(x["id"])

#converting the possible identifiers from str to int
possible_identifiers_string = [str(x) for x in possible_identifiers]

# CHECKPOINT 2: LOOK-UP PRODUCTS
while True:
    selected_id = input("Please input a product identifier:")
    if selected_id.upper() == "DONE":
        break
    else:
        if selected_id not in possible_identifiers_string:
            print("Hey, are you sure that product identifier is correct? Please try again!")
        else:
            selected_ids.append(selected_id)

        
#Printing the name of the grocery store 
print("----------------------------")
print("CARMEN'S GROCERY STORE")
print("WWW.CARMENS-GROCERY-STORE.COM")
print("----------------------------")

#Printing Checkout Time & Date
import datetime as dt
from datetime import datetime
current_date = dt.date.today()
print("CHECKOUT AT:",current_date,datetime.today().strftime("%I:%M %p"))
print("----------------------------")


## Information Display / Output
print("SELECTED PRODUCTS:")
for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print("... " + matching_product["name"] + " " + "(" + to_usd(matching_product["price"])+")")

# CHECKPOINT 3: PRINTING THE RECEIPT
subtotal = total_price
tax = total_price*0.06
TOTAL = subtotal+tax
print("----------------------------")
print("SUBTOTAL: " + to_usd(subtotal))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(TOTAL))
print("----------------------------")
print("THANKS, SEE YOU AGAIN!")
print("----------------------------")
