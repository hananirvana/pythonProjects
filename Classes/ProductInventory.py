"""
Product Inventory Project - Create an application which manages an
inventory of products. Create a product class which has a price, id,
and quantity on hand. Then create an inventory class which keeps track
of various products and can sum up the inventory value
"""

class Product:
    def __init__(self, price, id, quantity, name):
        self.price = price
        self.id = id
        self.quantity = quantity
        self.name = name

    def get_price(self):
        return self.price

    def get_id(self):
        return self.id

    def get_quantity(self):
        return self.quantity

    def get_name(self):
        return self.name


class Inventory:
    def __init__(self, filename='products.txt'):
        self.filename = filename

    def store_new_product(self, product):
        """
        Used to store a new product
        :param product: product to store to inventory, must have quantity, price and name
        :return: none; prints message that item has been stored
        """
        with open(self.filename, 'a') as f:
            f.write(f"({product.get_id()}) {product.get_name()} | ${product.get_price()}, qt: {product.get_quantity()}\n")
        print(f"Stored product {product.get_name()}!")

    def show_all_products(self):
        """
        Used to print out all products in inventory
        :return: none; prints products of inventory
        """
        try:
            with open(self.filename, 'r') as file:
                contents = file.read()
                print(contents)
        except FileNotFoundError:
            print("No products found.")

    def buy_item(self, product_name, quantity_to_buy):
        """
        Used to remove a quantity of an item in the inventory
        :param product_name: name of item to buy
        :param quantity_to_buy: amount of item that you want to buy
        :return: none; prints that item has been bought, and inventory is updated
        """
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            updated_lines = []
            product_found = False

            for line in lines:
                if product_name in line:
                    parts = line.split(", qt: ")
                    current_quantity = int(parts[1].strip())
                    new_quantity = current_quantity - quantity_to_buy

                    if new_quantity < 0:
                        print(f"Sorry, we don't have enough {product_name} to fulfil your request of {quantity_to_buy} {product_name}.")
                        return

                    updated_line = f"({self.get_product_id(product_name)}) {product_name} | ${self.get_product_price(product_name)}, qt: {new_quantity}\n"
                    updated_lines.append(updated_line)
                    product_found = True
                else:
                    updated_lines.append(line)

            if not product_found:
                print(f"Product {product_name} not found.")
                return

            with open(self.filename, 'w') as file:
                file.writelines(updated_lines)
            print(f"Here's your {quantity_to_buy} {product_name}! Thank you for buying from my store!")

        except FileNotFoundError:
            print("No products found.")

    def get_product_id(self, product_name):
        """
        Used to get the id of a product
        :param product_name: name of product id to find
        :return: returns id of product_name
        """
        with open(self.filename, 'r') as file:
            for line in file:
                if product_name in line:
                    return line.split()[0].strip('()')
        return None

    def get_product_price(self, product_name):
        """
        Used to get the price of a product
        :param product_name: name of product to get the price
        :return: returns price of product_name
        """
        with open(self.filename, 'r') as file:
            for line in file:
                if product_name in line:
                    return line.split('$')[1].split(',')[0]
        return None

    def restock_product(self, product_name, quantity_to_add):
        """
        Used to add more to an already-existing product in inventory
        :param product_name: name of product to RESTOCK. different from store_new_product()
        :param quantity_to_add: amount of products to RESTOCK.
        :return: none; prints message that product has been restocked
        """
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            updated_lines = []
            product_found = False

            for line in lines:
                if product_name in line:
                    parts = line.split(", qt: ")
                    current_quantity = int(parts[1].strip())
                    new_quantity = current_quantity + quantity_to_add

                    updated_line = f"({self.get_product_id(product_name)}) {product_name} | ${self.get_product_price(product_name)}, qt: {new_quantity}\n"
                    updated_lines.append(updated_line)
                    product_found = True
                else:
                    updated_lines.append(line)

            if not product_found:
                print(f"Product {product_name} not found.")
                return

            with open(self.filename, 'w') as file:
                file.writelines(updated_lines)
            print(f"Added {quantity_to_add} {product_name} to store!")

        except FileNotFoundError:
            print("No products found.")

    def create_product(self, price, quantity, name):
        """
        Used to create new product given the price, quantity and name. NOTE: automatically adds to inventory.
        :param price: price of new product
        :param quantity: quantity of new product
        :param name: name of new product (when using other functions, this is the name they will use)
        :return: none; prints message that item has been created and automatically added
        """
        # Determine the new product ID
        last_id = 0
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    if '(' in line and ')' in line:
                        current_id = int(line.split(')')[0].strip('('))
                        if current_id > last_id:
                            last_id = current_id
        except FileNotFoundError:
            print("No existing products file found. Starting with ID 0.")

        new_id = last_id + 1

        # Create a new Product object
        new_product = Product(price, new_id, quantity, name)

        # Store the new product
        self.store_new_product(new_product)
        print(f"Created and stored new product with ID {new_id}.")

# main uses:
def show():
    inventory = Inventory()
    inventory.show_all_products()

def restock(name,q):
    inventory = Inventory()
    inventory.restock_product(name, q)
    print("\nItems in store:")
    show()

def buy(name,q):
    inventory = Inventory()
    inventory.buy_item(name, q)
    print("\nItems in store:")
    show()

def put_new(product):
    """
    only used when you have a Product object already defined and you would like to add to inventory
    """
    inventory = Inventory()
    inventory.store_new_product(product)
    show()

def make(p,q,n):
    inventory = Inventory()
    inventory.create_product(p,q,n)
    print("\nItems in store:")
    show()

def has_numbers(i):
    return any(char.isdigit() for char in i)

if __name__ == '__main__':
    print("Welcome to the Local Grocery store!\nWe currently have")
    show()
    not_exit = True
    while not_exit:
        ch = input("What would you like to do? (b) - buy a product | (r) - restock product | (c) - create new product | (q) - quit -- ")
        if ch == "b":
            n = input("name of product to buy: ")
            i = int(input("amount you would like to buy: "))
            if has_numbers(n):
                print('ah sorry, i am asking for the name of product, not id.')
                continue
            buy(n, i)
        elif ch == "r":
            n = input("name of product to restock: ")
            i = int(input("amount you would like to restock: "))
            if has_numbers(n):
                print('ah sorry, i am asking for the name of product, not id.')
                continue
            restock(n, i)
        elif ch == "c":
            n = input("name of product to create: ")
            i = int(input("amount of product: "))
            p = int(input("price of an individual product: "))
            if has_numbers(n):
                print('ah sorry, i am asking for the name of product, not id.')
                continue
            make(p,i,n)
        elif ch == "q":
            print("Thank you for visiting my store!")
            break
        else:
            print("Unavailable option. Rerunning program...")

"""
TO WORK ON: 
- able to buy more products
- create the pricing of each products
- generate a bill
- change the wording of requests.
"""
