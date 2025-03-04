class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
    
    def __str__(self):
        return f"{self.name} - {self.price} TL (Stok: {self.stock})"