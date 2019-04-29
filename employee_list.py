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

        if len(self.emp_list) == 0:
            print('There is not data to update.')

            return

        self.show_emp()

        while True:
            print('Which employee-list do you want to update ?')
            number = int(input())
            if number == 0:
                break
            elif len(self.emp_list) >= number:
                print(self.emp_list[number - 1].get_name())
                name = input('name: ')
                self.emp_list[number - 1].set_name(name)
                print(self.emp_list[number - 1].get_phone())
                phone = input('phone: ')
                self.emp_list[number - 1].set_phone(phone)
                print(self.emp_list[number - 1].get_home())
                home = input('home: ')
                self.emp_list[number - 1].set_home(home)
                print(self.emp_list[number - 1].get_address())
                address = input('address: ')
                self.emp_list[number - 1].set_address(address)
                break


















