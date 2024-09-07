import hashlib

from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Auth:
    def __init__(self):
        self.__admin = {'username': 'admin', 'password': hashlib.sha256('admin'.encode()).hexdigest()}

    @log_decorator
    def create_users_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS users (
        ID BIGSERIAL PRIMARY KEY,
        FIRST_NAME VARCHAR(255) NOT NULL,
        LAST_NAME VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        phone_number BIGINT NOT NULL,
        ROLE VARCHAR(255) NOT NULL,
        IS_LOGIN BOOLEAN NOT NULL DEFAULT FALSE,
        CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP        
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def login(self):
        username: str = input('Username: ').strip()
        password: str = hashlib.sha256(input('Password: ').strip().encode('utf-8')).hexdigest()
        if username == self.__admin['username'] and password == self.__admin['password']:
            return {'is_login': True, 'role': 'admin'}
        return {'is_login': False}

    @log_decorator
    def logout(self):
        self.create_users_table()
        query = '''UPDATE users SET IS_LOGIN=FALSE;'''
        execute_query(query)
