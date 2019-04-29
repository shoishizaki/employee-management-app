import employee
import employee_list


def main():
    emp_func = employee_list.Employee_list()
    while True:
        print('######################')
        print('1.show employee list')
        print('2.add employee')
        print('3.update employee')
        print('4.delete employ')
        print('5.quit app')
        print('######################')
        print('~~~~~~~~~~~~~~~~~~~~~~')
        choose = input('choose-number: ')
        print('~~~~~~~~~~~~~~~~~~~~~~')
        if choose == '1':
            emp_func.show_emp()
        elif choose == '2':
            emp_func.add_emp()
        elif choose == '3':
            emp_func.update_emp()
        elif choose == '4':
            emp_func.del_emp()
        elif choose == '5':
            print('see you next time')
            break
        else:
            print('This number is not define.')




main()