import hashlib
import threading

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
        username: str = input('Username: ').strip()
        password: str = hashlib.sha256(input('Password: ').strip().encode('utf-8')).hexdigest()
        if username == self.__admin['username'] and password == self.__admin['password']:
            return {'is_login': True, 'role': 'admin'}
        return {'is_login': False}

    @log_decorator
    def register(self):
        first_name: str = input('First name: ').strip()
        last_name: str = input('Last name: ').strip()
        phone_number: int = int(input('Phone number ( +998 ) : '))
        print('Your account is being created...')
        username = get_username(name=first_name)

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
