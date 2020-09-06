class Store:
    def __init__(self, name, list_of_products=[]):
        self.name = name
        self.list_of_products = list_of_products
    
    # takes a product and adds it to the store
    def add_product(self, new_product):                            
        return self
    
    # remove product from store's list of products given id & print its info
    def sell_product(self, id):                                          
        return self
    
    # increases the price of each product by the percent_increase given
    def inflation(self, percent_increase):                  
        return self
    # updates all products matching given category by reducing price by  percent_discount given
    def set_clearance(self, category, percent_discount):    
        return self
    