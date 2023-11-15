'''
1.	You are tasked with developing a simplified e-commerce platform in Java. The platform will consist of various product categories, and customers can view product listings, add items to their shopping cart, and place orders. Your task is to implement the core classes for this platform.
Requirements:
a.	Create a base class named Product with the following attributes and methods:
Attributes:
•	productId (String)
•	productName (String)
•	price (double)
Methods:
•	Product(String productId, String productName, double price): A constructor to initialize the product attributes.
•	String toString(): A method to return a string representation of the product.
b.	Create three subclasses of Product: Electronics, Clothing, and Books. Each subclass should include additional attributes and methods specific to its category:
•	Electronics: Include attributes like warrantyPeriod and brand.
•	Clothing: Include attributes like size and color.
•	Books: Include attributes like author and genre.
c.	Implement polymorphism to allow customers to view product listings, add items to their shopping cart, and place orders. Use a common interface or superclass to handle products of different categories.
d.	Create a Cart class to represent a customer's shopping cart. This class should allow customers to add products, view the cart contents, and calculate the total cost of the items in the cart.
e.	Implement a Customer class to represent e-commerce customers. Customers should be able to browse products, add items to their shopping cart, view the cart, and place orders.
f.	Simulate a simple payment processing system. Customers should be able to complete their orders by making a payment. You can simulate this by printing a message indicating a successful payment
g.	Create a sample inventory of products, including electronics, clothing, and books, and allow customers to interact with the inventory.
'''
class Product:
    def __init__(self, product_id=None, product_name=None, price=None):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price
        
    @property
    def product_id(self):
        return self.__product_id
    
    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id
        
    @property
    def product_name(self):
        return self.__product_name
    
    @product_name.setter
    def product_id(self, product_name):
        self.__product_name = product_name
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price
        
    def __str__(self):
        return f"Product ID: {self.__product_id}, Product Name: {self.__product_name}, Price: {self.__price}"

    
class Electronics(Product):
    def __init__(self, product_id, product_name, price, warranty_period=None, brand=None):
        super().__init__(product_id, product_name, price)
        self.__warranty_period = warranty_period
        self.__brand = brand  
    def __str__(self):
        return super.__str() + f"Warranty Period {self.__warranty_period}, Brand: {self.__brand}"
    
class Clothing(Product):
    def __init__(self, product_id, product_name, price, size=None, color=None):
        super().__init__(product_id, product_name, price)
        self.__size = size
        self.__color = color  
    def __str__(self):
        return super.__str() + f"Size: {self.__size}, Color: {self.__color}"
    
class Books(Product):
    def __init__(self, product_id, product_name, price, author=None, genre=None):
        super().__init__(product_id, product_name, price)
        self.__author = author
        self.__genre = genre  
    def __str__(self):
        return super.__str() + f"Author: {self.__author}, Genre: {self.__genre}"
    
class Cart:
    def __init__(self):
        self.__items = []
        
    def add_items(self, product, quantity):
         self.__items.append({"product": product, "quantity": quantity})
        
    def display_items(self):
        return self.__items
    def calculate_cost(self):
        return sum([products["product"].price * products["quantity"] for products in self.__items])
        # total = 0
        # for products in self.__items:
        #     total += products["product"].price * products["quantity"]
        # return total
class User:
    def __init__(self, username):
        self.__username = username
    def __str__(self):
        return f"Username: {self.__username}"
    def discount(self):
        return 0
class Customer:
    def __init__(self):
        self.__choice = None
        self.__electronics = Electronics("123", "Selpon", 100, "12/12/2030", "Xiaomi")
        self.__clothing = Clothing("123", "Sinina", 100, "12/12/2030", "Chookstogo")
        self.__books = Books("123", "Librobasta", 100, "12/12/2030", "Gentle reminder")
        
    def browse(self):
        return f"{self.__electronics}\n{self.__clothing}\n{self.__books}"
        

# cart.add_items(electronics, 2)
# cart.add_items(electronics, 3)
# cart.add_items(electronics, 4)
# cart.add_items(electronics, 5)
# # print(cart.display_items())
# # print(cart.display_items()[1]["product"].product_id)
# # print(cart.display_items()[0]["quantity"])
# for items in cart.display_items():
#     print(f"{items["product"].product_name} - {items["quantity"]}")
# print(cart.calculate_cost())

