class Library_item:
    def __init__(self, item_id, title, available):
        self.__item_id = item_id
        self.__title = title
        self.__available = available
    
    def __str__(self):
        return f"Item ID: {self.__item_id}\nTitle: {self.__title}\nAvailability: {self.__available}"
    
    def check_out(self):
        if self.__available:
            self.__available = False
            return True
        else:
            return False
    def check_in(self):
        self.__available = True
        return self.__available
