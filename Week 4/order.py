from customer import Customer
from cart import Cart

class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart
        self.total_amount = cart.get_total()

    def place_order(self):
        if self.total_amount > 0:
            print("\nSipariş başarıyla oluşturuldu!")
            print(self.customer)
            print("\nSipariş detayları:")
            self.cart.display_cart()
            print(f"\nToplam Tutar: {self.total_amount} TL")
            self.cart.clear_cart()
        else:
            print("\nSepet boş, sipariş oluşturulamadı!")
