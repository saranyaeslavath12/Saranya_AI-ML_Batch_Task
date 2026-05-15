
def add_item(item, cart=[]):
    cart.append(item)
    return cart
print("--- Part A ---")
print(add_item("apple"))            #  ['apple']
print(add_item("banana"))           #  ['apple', 'banana'] 
print(add_item("milk", cart=["bread"])) # ['bread', 'milk'] 
print(add_item("eggs"))             # ['apple', 'banana', 'eggs'] 
print("\n")

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = [] # Create a new list every time
    cart.append(item)
    return cart

print("--- Part B ---")
print(add_item_fixed("apple"))      # ['apple']
print(add_item_fixed("banana"))     # ['banana'] 
print("\n")


def create_cart(owner, discount=0):
    # discount=0 is safe because integers are immutable.
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})

def update_price(price_tuple, new_price):
    try:
        price_tuple[1] = new_price
    except TypeError as e:
        print(f"Error caught: {e}")

def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]
    
    final_total = total * (1 - (cart["discount"] / 100))
    return final_total

print("--- Part C ---")
cart1 = create_cart("Alice", discount=10)
cart2 = create_cart("Bob")

add_to_cart(cart1, "Laptop", 1000)
add_to_cart(cart2, "Mouse", 50)

print(f"{cart1['owner']}'s Cart: {cart1['items']}")
print(f"{cart2['owner']}'s Cart: {cart2['items']}")
print(f"Alice Total: {calculate_total(cart1)}")
print(f"Bob Total: {calculate_total(cart2)}")
item_tuple = ("Keyboard", 100)
update_price(item_tuple, 120)
