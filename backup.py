import os 

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return f"{self.name},{self.price},{self.quantity}"
    
    def sell(self,amount):
        if amount<= self.quantity:
            self.quantity -=amount
            return True
        else:
            print(f"not enough quantity available for {self.name}. available:{self.quantity}")
            return False 
    def restock(self,amount):
        self.quantity+=amount
        return True
 
class ProductManager:
    def __init__(self ,filename):
        self.filename=filename
        self.products=[]
        self.load_products()
    

    def add_product(self,product):
        self.products.append(product)
        self.save_products()

    def save_products(self):
        with open(self.filename,'w') as f:
            for product in self.products:
                f.write(str(product)+"\n")

    def load_products(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r') as f:
                for line in f:
                    name,price,quantity=line.strip().split(',')
                    product=Product(name,float(price),int(quantity))
                    self.products.append(product)

    def display_products(self):
        if not self.products:
            print("no products found.!!")
        else:
            print("Product List")
            for i,product in enumerate (self.products ,start=1):
                print(f"{i}.Name:{product.name},price{product.price},Quantity:{product.quantity}")


    def sell_product(self,name,amount):
        for product in self.products:
            if product.name==name:
                return product.sell(amount)
        print(f"product {name} not found.")
        return False
    def restock_product(self,name,amount):
        for product in self.products:
            if product.name == name:
                return product.restock(amount)
        print(f"product {name} not found.")
        return False 


def main():
    filename="product.txt"
    manager=ProductManager(filename)

    while True:
        print("\n option:")
        print("1.add product")
        print("2.view product")
        print("3.sell product")
        print("4.restock product")
        print("5.exit ")

        choice=input("choose an option")
        if choice=="1":
            name=input("enter product name: ")
            price=float(input("enter product price: "))
            quantity=int(input("enter product quantity: "))
            product=Product(name,price,quantity)
            manager.add_product(product)
            print(f"Added product:{product}")

        elif choice=="2":
            manager.display_products()

        elif choice=="3":
            name=input("enter product name to sell")
            amount=int(input("enter quantity to sell"))
            if manager.sell_product(name,amount):
                print(f"sold {amount} of {name}")
                manager.save_products()
            else:
                print(f"Failed to sell {amount} of {name}")

        elif choice=="4":
            name=input("enter product name to restock")
            amount=int(input("enter quantity to restock"))
            if manager.restock_product(name,amount):
                print(f"restock {amount} of {name}")
                manager.save_products()
            else:
                print(f"Failed to restock {amount} of {name}")




        elif choice=="5":
            print("exiting...")
            break
        
        else:
            print("invalid option.please try again.")

if __name__=="__main__":
    main()










    
