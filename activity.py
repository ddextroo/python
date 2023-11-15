# Base class Product
class Product:
    
    #initialization
    def __init__(self,name=None,price=None):
        self.__name = name
        self.__price = price
        
    #getter and setter
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
    
    #method to retrieve description
    def get_description(self):
        return f"{self.__name} - ${self.__price}"

#Class inherit from product
class Clothing(Product):
    #initialization
    def __init__(self, name, price, size=None, color=None):
        super().__init__(name, price)
        self.__size = size
        self.__color = color 
    #getter and setter
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        self.__size = size
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color
     # method for retrieving
    def get_description(self):
        return f"{super().name}({self.__size}, {self.__color}) - ${super().price - (super().price * 0.05) if self.__size.lower() == "xs".lower() or self.__color.lower() == "red".lower() else super().price}"
# class inherit from clothing
class Footwear(Clothing):
    #initialization
    def __init__(self, name, price, size, color, typee=None):
        super().__init__(name, price, size, color)
        self.__type = typee
    #method for retrieving
    def get_description(self):
        return f"{super().get_description()} - {self.__type}"
#class inherit from clothing
class Outwear(Clothing):
    #initialization
    def __init__(self, name, price, size, color, style=None):
        super().__init__(name, price, size, color)
        self.__style = style
    #method for retrieving
    def get_description(self):
        return f"{super().get_description()} - {self.__style}"
#class inherit from product
class Furniture(Product):
    #initialization
    def __init__(self, name, price, material=None):
        super().__init__(name, price)
        self.__material = material
        
    # getter and setter
    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self, material):
        self.__material = material
        
    #method for retrieving
    def get_description(self):
        return f"{super().name}({self.__material}) - ${super().price - (super().price * 0.10) if self.__material.lower() == "wood".lower() else super().price}"
#class inherit from furniture
class Chairs(Furniture):
    def __init__(self, name, price, material, style=None):
        super().__init__(name, price, material)
        self.__style = style
    #method for retrieving
    def get_description(self):
        return f"{super().get_description()} - {self.__style}"
#class inherit from furniture
class Tables(Furniture):
    #initialization
    def __init__(self, name, price, material, typee=None):
        super().__init__(name, price, material)
        self.__type = typee
    #method for retrieving
    def get_description(self):
        return f"{super().get_description()} - {self.__type}"
#class inherit from furniture
class Beds(Furniture):
    #initialization
    def __init__(self, name, price, material, size=None):
        super().__init__(name, price, material)
        self.__size = size
    #method for retrieving
    def get_description(self):
        return f"{super().get_description()} - {self.__size}"
#class inherit from product
class Toys(Product):
    #initialization
    def __init__(self, name, price, age_group):
        super().__init__(name, price)
        self.__age_group = age_group
    # getter and setter
    @property
    def age_group(self):
        return self.__age_group
    @age_group.setter
    def age_group(self, age_group):
        self.__age_group = age_group
    # method for retrieving
    def get_description(self):
        return f"{super().name}({self.__age_group}) - ${super().price}"
#class inherit from toys
class ActionFigures(Toys):
    #initialization
    def __init__(self, name, price, age_group, character=None):
        super().__init__(name, price, age_group)
        self.__character = character
    
    #method for retrieving
    def get_description(self):
        return f"{super().get_description()} - {self.__character}"
#class inherit from toys
class Dolls(Toys):
    #initialization
    def __init__(self, name, price, age_group, typee=None):
        super().__init__(name, price, age_group)
        self.__type = typee
    # method for retrieving
    def get_description(self):
        return f"{super().get_description()} - {self.__type}"

#declaring objects
product = Product("T-Sshirt", 20.00)
clothing = Clothing("T-Sshirt", 20.00, "M".lower(), "Red".lower())
footwear = Footwear("T-aShirt", 20.00, "M".lower(), "Red".lower(), "Sneakers")
outwear = Outwear("T-Shsirt", 20.00, "M".lower(), "Green".lower(), "jacket")
furniture = Furniture("Bangko", 220.00, "Wood".lower())
chairs = Chairs("Bangko", 220.00, "Wood".lower(), "dining chair")
tables = Tables("Bangko", 220.00, "Wood".lower(), "coffee table")
beds = Beds("Bangko", 220.00, "Wood".lower(), "queen")
toys = Toys("Robot", 2210.00, "ambot")
actionfigures = ActionFigures("Robot", 2210.00, "ambot", "ako")
dolls = Dolls("Robot", 2210.00, "ambot", "fashion doll")


# products = [clothing, footwear, outwear, furniture, chairs, tables, beds, toys, actionfigures, dolls]
products = [product, clothing,footwear, outwear, furniture, chairs, tables, beds, toys, actionfigures, dolls]


#duck typing
#loop the objects to print the same methods/function
for product in products:
    print(product.get_description())