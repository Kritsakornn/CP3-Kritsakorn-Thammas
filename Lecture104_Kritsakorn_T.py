class Customer:
    name = ""
    lastName = ""
    age = 0;

    def addCart(self):
        print("Added to product to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Kritsakorn"
customer1.lastName = "Thammas"
customer1.addCart()

customer2 = Customer()
customer2.name = "Thomas"
customer2.lastName = "Mation"
customer2.addCart()

customer3 = Customer()
customer3.name = "Alex"
customer3.lastName = "Agenda"
customer3.addCart()

customer4 = Customer()
customer4.name = "Anaconda"
customer4.lastName = "Obo"
customer4.addCart()