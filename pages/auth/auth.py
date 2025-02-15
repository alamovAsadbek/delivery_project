import hashlib
import threading

from psycopg2 import sql

from components.color_text.color_text import print_bold
from components.random_password.generate_password import generate_password
from components.random_username.generate_username import get_username
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator
from pages.auth.tables.tables import Tables


class Auth:
    def __init__(self):
        self.__admin = {'username': 'admin', 'password': hashlib.sha256('admin'.encode()).hexdigest()}
        self.__tables = Tables()

    @log_decorator
    def login(self):
        tables = ['users', 'restaurants', 'branch']
        username: str = input('Username: ').strip()
        password: str = hashlib.sha256(input('Password: ').strip().encode('utf-8')).hexdigest()
        print("Checked...")
        if username == self.__admin['username'] and password == self.__admin['password']:
            return {'is_login': True, 'role': 'admin'}
        for table in tables:
            query = sql.SQL("SELECT * FROM {} WHERE username=%s and password=%s").format(sql.Identifier(table))
            params = (username, password)
            result_get = execute_query(query, params, fetch='one')
            if result_get is not None:
                query = '''
                UPDATE {} set is_login=TRUE WHERE id=%s
                '''.format(table)
                params = (result_get['id'],)
                threading.Thread(target=execute_query, args=(query, params)).start()
                print("Login successful!")
                return {'is_login': True, 'role': result_get['role']}
        return {'is_login': False, 'role': 'user'}

    @log_decorator
    def register(self):
        first_name: str = input('First name: ').strip()
        last_name: str = input('Last name: ').strip()
        phone_number: int = int(input('Phone number ( +998 ) : '))
        print('Your account is being created...')
        username = get_username(name=first_name, table_name='users')
        password = generate_password()
        hash_password = hashlib.sha256(password.__str__().encode('utf-8')).hexdigest()
        print(f'\nYour username is {print_bold(username, 32)} '
              f'and password is {print_bold(password, 32)}\n')
        query = '''
        INSERT INTO users(FIRST_NAME, LAST_NAME, username, password, phone_number, ROLE)
        VALUES (%s, %s, %s, %s, %s, %s);
        '''
        params = (first_name, last_name, username, hash_password, phone_number, 'user')
        threading.Thread(target=execute_query, args=(query, params)).start()
        print("Registered successfully")
        return True

    @log_decorator
    def create_tables(self):
        self.__tables.create_restaurants_table()
        self.__tables.create_branch_table()
        self.__tables.create_products_table()
        self.__tables.create_baskets_table()
        self.__tables.create_basket_items_table()
        self.__tables.create_orders_table()
        self.__tables.create_order_items_table()
        self.__tables.create_requests_table()
        return True

    @log_decorator
    def logout(self):
        threading.Thread(target=self.create_tables).start()
        self.__tables.create_users_table()
        query = '''UPDATE users SET IS_LOGIN=FALSE;'''
        execute_query(query)
