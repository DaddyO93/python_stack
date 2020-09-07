class Products:
    def __init__(self, product_info):
        self.category = product_info.get("category")
        self.name = product_info.get("name")             
        self.price = product_info.get("price")
        self.id = 0
    
    # updates the product's price
    def update_price(self, percent_change, is_increased=False):
        print("\n","*"*50, "\n")
        print("Price changes are happening!")
        print("\n","*"*50, "\n")
        if is_increased==True:
            self.price = self.price*percent_change+self.price
            return self
        else:
            self.price = self.price-self.price*percent_change
            return self
        return self

    # print the name of the product, its category, and its price
    def print_info(self):
        print(f"Product Category: {self.category}")
        print(f"Product Name: {self.name}")
        print(f"Product Price: ${self.price}")
        print("\n","*"*50, "\n")
        return self
