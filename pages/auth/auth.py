import hashlib

from main_files.decorator.decorator_func import log_decorator


class Auth:
    def __init__(self):
        self.__admin = {'username': 'admin', 'password': 'admin'}

    @log_decorator
    def login(self):
        username: str = input('Username: ').strip()
        password: str = hashlib.sha256(input('Password: ').strip().encode('utf-8')).hexdigest()
