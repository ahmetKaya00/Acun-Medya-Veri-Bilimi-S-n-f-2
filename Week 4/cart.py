from product import Product

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.update_stock(quantity):
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}
        else:
            print(f"Yetersiz stok: {product.name}")

    def remove_product(self, product_name):
        if product_name in self.items:
            product = self.items[product_name]['product']
            quantity = self.items[product_name]['quantity']
            product.stock += quantity
            del self.items[product_name]

    def display_cart(self):
        if not self.items:
            print("Sepetiniz boş.")
        else:
            for item in self.items.values():
                print(f"{item['product'].name} - {item['quantity']} adet - {item['product'].price * item['quantity']} TL")

    def get_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items.values())

    def clear_cart(self):
        self.items.clear()
