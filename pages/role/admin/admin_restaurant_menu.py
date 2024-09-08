import hashlib
import threading
import time

from components.color_text.color_text import print_bold
from components.pagination.pagination import Pagination
from components.random_password.generate_password import generate_password
from components.random_username.generate_username import get_username
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
        SELECT r.id, r.name, r.username, r.phone_number, r.company_fee, u.first_name as owner_first_name, 
        u.last_name as owner_last_name, u.username as owner_username, u.phone_number as owner_number
          FROM restaurants r
        INNER JOIN users u on r.OWNER_ID = u.ID
        '''
        result = execute_query(query, fetch='all')
        pagination = Pagination(table_name='restaurants', data=result,
                                table_keys=['id', 'name', 'username', 'phone_number', 'company_fee',
                                            'owner_first_name', 'owner_last_name', 'owner_username', 'owner_number'],
                                display_keys=['RESTAURANT ID', 'RESTAURANT NAME', 'RESTAURANT USERNAME',
                                              'RESTAURANT PHONE', 'COMPANY FEE (%) ', 'OWNER FIRST NAME',
                                              'OWNER LAST NAME',
                                              'OWNER USERNAME', 'OWNER NUMBER'])
        if not pagination.page_tab():
            return False
        return True

    @log_decorator
    def create_restaurant(self, update_data=None):
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
        print("Waiting...")
        get_data = self.get_data(user_id.__str__(), table_name='users', role='owner')
        if get_data is None:
            print('User does not exist')
            return False
        print(f"Owner ID: {get_data['id']}\nOwner full name: {get_data['last_name']} {get_data['first_name']}\n"
              f"Owner username: {get_data['username']}")
        print("Creating restaurant...")
        username = update_data['username']
        if update_data is None:
            username = get_username(table_name='restaurants', name=name, key='restaurant')
        password = generate_password()
        print(f"{name.capitalize()} restaurant username: {print_bold(username, 34)} "
              f"and password: {print_bold(password, 34)}")
        has_password = hashlib.sha256(password.__str__().encode('utf-8')).hexdigest()
        query = '''
        INSERT INTO restaurants (NAME, USERNAME, PASSWORD, ROLE, PHONE_NUMBER, COMPANY_FEE, OWNER_ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        params = (name, username, has_password, 'restaurant', phone_number, company_fee, get_data['id'])
        if update_data is not None:
            query = '''
            UPDATE restaurants
            SET 
                NAME = %s,
                USERNAME = %s,
                PASSWORD = %s,
                ROLE = %s,
                PHONE_NUMBER = %s,
                COMPANY_FEE = %s
            WHERE 
                ID = %s;
            '''
            params = (name, username, has_password, 'restaurant', phone_number, company_fee, update_data['id'])
        threading.Thread(target=execute_query, args=(query, params)).start()
        if update_data is None:
            print("Restaurant created successfully")
        else:
            print("Restaurant updated successfully")
        return True

    @log_decorator
    def update_restaurant(self):
        if not self.show_all_restaurants():
            return False
        restaurant_id = int(input("Enter the restaurant ID or enter 0 to exit: ").strip())
        if restaurant_id == 0:
            print('Exit')
            return False
        print("Waiting...")
        get_data = self.get_data(restaurant_id, table_name='restaurants')
        if get_data is None:
            print("Restaurant does not exist")
            return False
        self.create_restaurant(update_data=get_data)
        return True
