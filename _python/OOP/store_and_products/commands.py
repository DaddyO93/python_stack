from products import Products
from store import Store

apple = Products({"category":"fruit", "name":"apple", "price":.5})
orange = Products({"category":"fruit", "name":"orange", "price":.8})
banana = Products({"category":"fruit", "name":"banana", "price":.6})

carrot = Products({"category":"vegetable", "name":"carrot", "price":1})
potato = Products({"category":"vegetable", "name":"potato", "price":2})
onion = Products({"category":"vegetable", "name":"onion", "price":1.5})

hat = Products({"category":"clothing", "name":"hat", "price":10})
boots = Products({"category":"clothing", "name":"boots", "price":20})
gloves = Products({"category":"clothing", "name":"gloves", "price":6})

store_1 = Store("Bob's Store")
store_2 = Store("Bill's Store")

store_1.add_product(apple).add_product(carrot).add_product(gloves).add_product(onion).list_of_inventory()
store_1.sell_product(3).list_of_inventory().inflation(.2).list_of_inventory().set_clearance("clothing", .1).list_of_inventory()
