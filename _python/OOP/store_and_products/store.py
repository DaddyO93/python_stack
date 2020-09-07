from random import randint
from products import Products

class Store:
    def __init__(self, name, list_of_products=[]):
        self.name = name
        self.list_of_products = list_of_products
    
    # takes a product and adds it to the store
    def add_product(self, new_product):
        new_product.id = len(self.list_of_products) # + randint(1, 10)
        self.list_of_products.append(new_product)
        return self
    
    # remove product from store's list of products given id & print its info
    def sell_product(self, id):
        for i in self.list_of_products:
            if i.id == id:
                Products.print_info(i)
                self.list_of_products.remove(i)
                print("\nThank you for your purchase!\n")
                print("\n","*"*50, "\n")
                in_inventory=True
            else:
                in_inventory = False
                pass
        if in_inventory == False:
            print("\nThat ID is not in our inventory!")
            print("\n","*"*50, "\n")
        return self
    
    # increases the price of each product across the store by the percent_increase given
    def inflation(self, percent_increase):
        for i in self.list_of_products:
            i.update_price(percent_increase, True)
        return self
    
    def list_of_inventory (self):
        print("\n","*"*50, "\n")
        print(f"Inventory for {self.name}\n")
        for i in self.list_of_products:
            print(i.name, "$"+str(i.price))
            print(f"ID #: {i.id}\n")
        print("\n","*"*50, "\n")
        return self
    
    # updates all products matching given category by reducing price by  percent_discount given
    def set_clearance(self, category, percent_discount):
        for i in self.list_of_products:
            if i.category == category:
                i.update_price(percent_discount)
        return self
    
    