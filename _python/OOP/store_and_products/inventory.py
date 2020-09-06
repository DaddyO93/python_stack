from products import Products

apple = Products({"name":"apple", "category":"fruit", "price":.5})
orange = Products({"name":"orange", "category":"fruit", "price":.8})
banana = Products({"name":"banana", "category":"fruit", "price":.6})

carrot = Products({"name":"carrot", "category":"vegetable", "price":1})
potato = Products({"name":"potato", "category":"vegetable", "price":2})
onion = Products({"name":"onion", "category":"vegetable", "price":1.5})

hat = Products({"name":"hat", "category":"clothing", "price":10})
boots = Products({"name":"boots", "category":"clothing", "price":20})
gloves = Products({"name":"gloves", "category":"clothing", "price":6})


hat.print_info().update_price(.2, True).print_info()
