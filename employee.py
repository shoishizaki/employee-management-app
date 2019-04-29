class Employee():
    def __init__(self, name, phone, home, address):
        self.name = name
        self.phone = phone
        self.home = home
        self.address = address

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_home(self):
        return self.home

    def set_home(self, home):
        self.home = home

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address
