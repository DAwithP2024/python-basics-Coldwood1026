# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}
import re

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))



def display_products(products_list):
    for index, (name, price) in enumerate(products_list):
        print(f"{index + 1}. {name} - ${price}")


def display_categories():
    for index, category in enumerate(products.keys()):
        print(f"{index + 1}. {category}")
    choice = input("Select a category by number: ")
    return int(choice) - 1 if choice.isdigit() else None



def add_to_cart(cart, product, quantity):
    cart.append((*product, quantity))


def display_cart(cart):
    total_cost = 0
    for name, price, quantity in cart:
        cost = price * quantity
        print(f"{name} - ${price} x {quantity} = ${cost}")
        total_cost += cost
    print(f"Total cost: ${total_cost}")



def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}\nEmail: {email}\nItems Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}\nDelivery Address: {address}\nYour items will be delivered in 3 days.\nPayment will be accepted upon delivery.")


def validate_name(name):
    return bool(re.match(r'^[A-Za-z]+\s[A-Za-z]+$', name))





import re

def validate_email(email):
    # 允许没有顶级域名的简单格式
    if email.strip() == "":
        return False
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})?$'
    return re.match(regex, email) is not None




def main():
    cart = []
    while True:
        display_categories()
        category_index = int(input("Choose a category (or 0 to exit): ")) - 1
        if category_index == -1:
            break
        selected_category = list(products.values())[category_index]
        display_products(selected_category)
        product_choice = int(input("Select a product by number: ")) - 1
        product = selected_category[product_choice]
        quantity = int(input("Enter quantity: "))
        add_to_cart(cart, product, quantity)
        display_cart(cart)

    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
