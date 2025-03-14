import sys
from product import Product
from customer import Customer
from cart import Cart
from order import Order

def main():
    products = [
        Product("Laptop", 15000, 5),
        Product("Telefon", 10000, 10),
        Product("Kulaklık", 500, 20)
    ]

    name = input("Müşteri Adınızı Girin: ")
    email = input("E-posta adresinizi girin: ")
    customer = Customer(name, email)

    cart = Cart()

    while True:
        print("\nÜrünler:")
        for i, product in enumerate(products):
            print(f"{i+1}. {product}")

        print("\nYapmak İstediğiniz İşlemi Seçiniz:")
        print("1. Ürün ekle")
        print("2. Ürün çıkar")
        print("3. Sepeti görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")

        choice = input("Seçiminizi Yapın: ")

        if choice == "1":
            try:
                product_index = int(input("Hangi ürünü eklemek istiyorsunuz? (Numara): ")) - 1
                if 0 <= product_index < len(products):
                    quantity = int(input("Kaç adet eklemek istiyorsunuz?: "))
                    cart.add_product(products[product_index], quantity)
                else:
                    print("Geçersiz ürün numarası!")
            except ValueError:
                print("Geçersiz giriş, tekrar deneyin!")


if __name__ == "__main__":
    main()