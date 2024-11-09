import os
import product as pro

class ProductManager:
    def __init__(self ,filename):
        self.filename=filename
        self.products=[]
        self.load_products()
    

            
    def add_product(self,name,product):
        # for product in self.products:
        #     if product.name==name:
        #         print("product name already exist")
        #         return False
        #     else:
        #         return True
                
        self.products.append(product)
        self.save_products()

    def save_products(self):
            #print("no products found.!!")
        with open(self.filename,'w') as f:
            for product in self.products:
                 f.write(str(product)+"\n")

    def load_products(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r') as f:
                for line in f:
                    name,price,quantity=line.strip().split(',')
                    product=pro.Product(name,float(price),int(quantity))
                    self.products.append(product)

    def display_products(self):
        if not self.products:
            print("no products found.!!")
        else:
            print("Product List")
            print(self.products.index("name"))
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
    # def delete_product(self,name):
    #     for product in self.products:
    #         if product.name==name:
    #             print(self.products.remove(name))
                
    #     print(f"product cannot be found!!")
    #     print(self.products.remove(product))
    #     return False


    # def delete_product(self,name):
    #     if os.path.exists(self.filename):
    #         with open(self.filename,'r')as file:
    #             lines=file.readlines()
    #         with open(self.filename,'w') as file:
    #             for line in lines:
    #                 if name not in line:
    #                     file.write(line)
                        
    #                 else:
    #                     print(f"product{name}found and deleted.")
    #                 if name in self.products:
    #                     self.products.pop(name)                    
    #             return False
                        


    # def delete_product(self,product,name):
    #     for product in products:
    #         product.remove(products)
    #         print(f"product {name} deleted succesfully")
    #         return True
    #     print(f"product {name} not found")
    #     return False


    # def delete_product(self,name):
    #     try:
    #         index=self.product.index(name)
    #         del self.products[index]
    #         self.save_products()
    #         print(f"product {name} deleted sucessfully.")
    #     except ValueError:
    #         print(f"product {name} not found no deleted.")





    # def delete_product(self,name):
    #     if name in self.products:
    #         del self.products[name]
    #         index=self.products.index(name)
    #         del self.products[index]
    #         self.save_products()
    #         print(f"product {name} deleted.")
    #     else:
    #         print(f"product {name} not deleted")        


    def delete_product(self,name):
        for index,product in enumerate(self.products):
            if product.name==name:
                del self.products[index]
                self.save_products()
                print(f"product {name} deleted successfully")
                return True
        print (f"product {name} not found not deleted")
        return False 