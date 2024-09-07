import hashlib
import threading

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
    def logout(self):
        threading.Thread(target=self.__tables.create_restaurants_table).start()
        self.__tables.create_users_table()
        query = '''UPDATE users SET IS_LOGIN=FALSE;'''
        execute_query(query)
