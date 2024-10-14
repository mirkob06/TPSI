class Product:
    product_count = 0

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        Product.product_count += 1

    def product_total(self):
        return self.price * self.quantity
    
    @staticmethod
    def count():
        print(f"The number of products is: {Product.product_count}")

product1 = Product("Nutella", 2, 7)
product2 = Product("Zucchero", 3, 4)

print(f"{product1.name} total value: {product1.product_total()}")  
print(f"{product2.name} total value: {product2.product_total()}")  

Product.count()