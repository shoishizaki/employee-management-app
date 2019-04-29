import employee


class Employee_list():
    def __init__(self):
        self.emp_list =[]

    def show_emp(self):
        if self.emp_list == []:
            print('There is no employee in the list.')
        else:
            i = range(1, len(self.emp_list)+1)
            count = 0
            print('----------------------------')
            for ls in self.emp_list:
                print(i[count],'name:',ls.get_name(), ',',
                      'phone:',ls.get_phone(), ',',
                      'home:',ls.get_home(), ',',
                      'address:',ls.get_address())
                count += 1
            print('----------------------------')


    def add_emp(self):
        name = input('name: ')
        phone = input('phone: ')
        home = input('home: ')
        address = input('address: ')
        emp = employee.Employee(name, phone, home, address)
        self.emp_list.append(emp)
 

    def del_emp(self):
        while True:
            if len(self.emp_list) == 0:
                print('There is not data to delete.')
                break
            else:
                print('Which employee-list do you want to delete ? ')
                print(0, 'finish')
                for i, ls in enumerate(self.emp_list, 1):
                    print(i, ls.get_name())
            number = int(input())
            if number == 0:
                print('Thank you.')
                break
            elif len(self.emp_list) >= number:
                del self.emp_list[number - 1]
            else:
                print('This number is not define.')

    def update_emp(self):
        while True:
            if len(self.emp_list) == 0:
                print('There is not data to update.')
                break
            else:
                print('Which employee-list do you want to delete ?')
                print(0, 'finish')
                self.show_emp()
                number = int(input())
                if number == 0:
                    print('Thank you.')
                    break
                elif len(self.emp_list) >= number:
                    print('Which item do you want to update ?')
                    print(0,"I want to update another person's date.")
                    print(1, 'name')
                    print(2, 'phone')
                    print(3, 'home')
                    print(4, 'address')
                    item_ls = int(input())
                    if item_ls == 0:
                        print('Return to the people choice.')
                    elif item_ls == 1:
                        print(self.emp_list[number - 1].get_name())
                        name = input('name: ')
                        self.emp_list[number - 1].set_name(name)
                    elif item_ls == 2:
                        print(self.emp_list[number - 1].get_phone())
                        phone = input('phone: ')
                        self.emp_list[number - 1].set_phone(phone)
                    elif item_ls == 3:
                        print(self.emp_list[number - 1].get_home())
                        home = input('home: ')
                        self.emp_list[number - 1].set_home(home)
                    elif item_ls == 4:
                        print(self.emp_list[number - 1].get_address())
                        address = input('address: ')
                        self.emp_list[number - 1].set_address(address)
                    else:
                        print('This number is not define.')
                        print('Please try again from the beginning.')
                else:
                    print('This number is not define.')


























