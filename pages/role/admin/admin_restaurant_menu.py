import time

from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator
from pages.role.admin.admin_user_menu import AdminUserMenu


class AdminRestaurantMenu:
    def __init__(self):
        self.__user_menu = AdminUserMenu()

    @log_decorator
    def get_data(self, data_id, table_name, role=None):
        if role is None:
            query = '''
            SELECT * FROM {} WHERE id=%s
            '''.format(table_name)
            return execute_query(query, (data_id,), fetch='one')
        query = '''
        SELECT * FROM {} WHERE id=%s and role=%s
        '''.format(table_name)
        return execute_query(query, (data_id, role,), fetch='one')

    @log_decorator
    def show_all_restaurants(self):
        print("Waiting...")
        query = '''
        SELECT * FROM restaurants
        INNER JOIN users u on restaurants.OWNER_ID = u.ID
        '''
        result = execute_query(query, fetch='all')
        print(result)

    @log_decorator
    def create_restaurant(self):
        name = input("Enter restaurant name: ").strip()
        phone_number = int(input("Enter phone number ( +998 ): ").strip())
        company_fee = int(input("Enter company fee (0-100): ").strip())
        print("Waiting...")
        while True:
            query = '''
                    SELECT * FROM users
                    WHERE role='owner'
                    '''
            result = execute_query(query, fetch='all')
            pagination = Pagination(table_name='users', data=result,
                                    table_keys=['id', 'first_name', 'last_name', 'username', 'phone_number'],
                                    display_keys=['ID', 'FIRST NAME', 'LAST NAME', 'USERNAME', 'PHONE NUMBER'])
            pagination.page_tab()
            print('\n1. Add new owner\n2. Enter user id')
            user_choice = int(input("Choose menu: ").strip())
            if user_choice == 1:
                self.__user_menu.create_user()
                print("User created successfully")
                time.sleep(5)
                continue
            elif user_choice == 2:
                break
            print('Wrong input')
        user_id: int = int(input("Enter user id: ").strip())
        get_data = self.get_data(user_id.__str__(), table_name='users', role='owner')
        if get_data is None:
            print('User does not exist')
            return False
        print(f"Owner ID: {get_data['id']}\nOwner full name: {get_data['last_name']} {get_data['first_name']}\n"
              f"Owner username: {get_data['username']}")
