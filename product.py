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
    # def delete(self,product):
    #     self.name.pop(product)