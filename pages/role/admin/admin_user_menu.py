import hashlib
import threading

from components.color_text.color_text import print_bold
from components.pagination.pagination import Pagination
from components.random_password.generate_password import generate_password
from components.random_username.generate_username import get_username
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminUserMenu:
    @log_decorator
    def show_all_users(self):
        pagination = Pagination(table_name='users',
                                table_keys=['id', 'first_name', 'last_name', 'phone_number', 'role', 'created_at'],
                                display_keys=['ID', 'FIRST_NAME', 'LAST_NAME', 'PHONE_NUMBER', 'ROLE', 'created_at'])
        pagination.page_tab()
        return True

    @log_decorator
    def create_user(self):
        first_name = input('First Name: ').strip()
        last_name = input('Last Name: ').strip()
        phone_number = input('Phone Number: ').strip()
        role = 'user'
        while True:
            print("\nChoose user role")
            print("1. User\t2. Courier\t3. Owner restaurant")
            user_choice = int(input("Enter your choice: ").strip())
            if user_choice == 1:
                role = 'user'
            elif user_choice == 2:
                role = 'courier'
            elif user_choice == 3:
                role = 'owner'
            else:
                print("Invalid choice")
                continue
            break
        print("Creating an account...")
        if role != 'user':
            username = get_username(table_name='users', name=first_name, key=role)
        else:
            username = get_username(table_name='couriers', name=first_name)
        password = generate_password()
        print(f'{role.capitalize()} username: {print_bold(username, 32)} and password: {print_bold(password, 32)}')
        hash_password = hashlib.sha256(password.__str__().encode('utf-8')).hexdigest()
        query = '''
                INSERT INTO users(FIRST_NAME, LAST_NAME, username, password, phone_number, ROLE)
                VALUES (%s, %s, %s, %s, %s, %s);
        '''
        params = (first_name, last_name, username, hash_password, phone_number, role)
        threading.Thread(target=execute_query, args=(query, params)).start()
        print(f"{role.capitalize()} created successfully")
        return True

    @log_decorator
    def update_user(self):
        print("Choose user ID")
        self.show_all_users()
        user_id = int(input('Enter your user ID or 0 to log out: ').strip())
        if user_id == 0:
            print("Exit")
            return True
        print("Get data...")
        result_get = self.get_data(table_name='users', table_id=user_id)
        if result_get is None:
            print("Invalid user ID")
            return False
        print(f"\nID: {result_get['id']}\nFirst name: {result_get['first_name']}\n"
              f"Last name: {result_get['last_name']}\nUsername: {result_get['username']}\n"
              f"Phone number: {result_get['phone_number']}\nRole: {result_get['role']}\n")
        password = input('Enter new password: ').strip()
        while password == '' or len(password) < 4:
            print("Invalid password, Must be at least 4 characters")
            password = input('Enter new password: ').strip()
        hash_password = hashlib.sha256(password.__str__().encode('utf-8')).hexdigest()
        query = '''
        UPDATE users SET password=%s WHERE id=%s;
        '''
        params = (hash_password, user_id)
        threading.Thread(target=execute_query, args=(query, params)).start()
        print("Updated successfully")
        return True

    @log_decorator
    def get_data(self, table_name: str, table_id: int = None):
        if table_id is not None:
            query = '''
            SELECT * FROM {} WHERE id = %s;
            '''.format(table_name)
            params = (table_id,)
            return execute_query(query, params, fetch='one')
        query = '''
        SELECT * FROM {};
        '''.format(table_name)
        return execute_query(query)
