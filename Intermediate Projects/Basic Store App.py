class Store:
    store_name = "SwiftBuy Store"

    def __init__(self):
        self.products = []
        self.balance = 10000

    def add_products(self, product_name, product_price):
        self.products.append((product_name, product_price))
        print(f"{product_name} added for ${product_price}")
        
    def available_products(self):
        if not self.products:
            return "No Products available!"
            
        else:
            print("\nAvailable Products:")
            for product in self.products:
                return f"- {product[0]}: ${product[1]}"
                

    def buy_products(self, buy_product):
        for product in self.products:
            if product[0] == buy_product:
                if self.balance > product[1]:
                    self.balance -= product[1]
                    self.products.remove(product)
                    print(f"\n{buy_product} purchased!")
                else:
                    print("Insufficient Balance!")

    def store_balance(self, store_balance):
        self.balance = store_balance
        
    def get_balance(self):
        return f"Available Balance: ${self.balance}"


store = Store()
print(store.store_name)


store.add_products('Laptop', 1200)
store.add_products("Phone", 800)
store.add_products("Headphones", 150)
store.add_products("Ipad", 1000)

store.buy_products("Headphones")
store.buy_products('Laptop')
store.buy_products("Phone")


print(store.get_balance())
print(store.available_products())
