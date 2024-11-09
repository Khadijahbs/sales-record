import os 
import product as pro
import ProductManager as pm

def main():
    filename="product.txt"
    manager=pm.ProductManager(filename)

    while True:
        print("\n option:")
        print("1.add product")
        print("2.view product")
        print("3.sell product")
        print("4.restock product")
        print("5.delete")
        print("6.exiting...")

        choice=input("choose an option: ")
        if choice=="1":
            name=input("enter product name: ")
            price=float(input("enter product price: "))
            quantity=int(input("enter product quantity: "))
            product=pro.Product(name,price,quantity)
            manager.add_product(name,product)
            if product.name==name:
                print("product already exist")
            else:
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

        # elif choice=="5":
        #     name=input("enter the product name you want to delete: ")
        #     if manager.delete_product(name):"
        #         print(f"product {name} deleted successfully")

        elif choice=="5":
            name=input("enter the product name you want to delete: ")
            if manager.delete_product(name):
                print(f"product {name} deleted successfully ")
            else:
                print(f"product {name} not found in the list")


        elif choice=="6":
            print("exiting...")
            break
        
        else:
            print("invalid option.please try again.")

if __name__=="__main__":
    main()










    
