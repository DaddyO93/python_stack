# import store_and_products.inventory as inventory


class Products:
    def __init__(self, product_info):
        self.category = product_info.get("category")             
        self.name = product_info.get("name")
        self.price = product_info.get("price")
    
    # updates the product's price
    def update_price(self, percent_change, is_increased):
        if is_increased==True:
            print("The price is going up!")
            self.price = self.price*percent_change+self.price
            return self
        else:
            print("\n", "^"*5, "The price stayed the same!", "^"*5, "\n")
            return self
        return self

    # print the name of the product, its category, and its price
    def print_info(self):
        print("\n","*"*50, "\n")
        print(f"Product Category: {self.category}")
        print(f"Product Name: {self.name}")
        print(f"Product Price: ${self.price}")
        print("\n","*"*50, "\n")
        return self

