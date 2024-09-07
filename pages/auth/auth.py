import hashlib

from main_files.decorator.decorator_func import log_decorator


class Auth:
    @log_decorator
    def login(self):
        username: str = input('Username: ').strip()
        password: str = hashlib.sha256(input('Password: ').strip().encode('utf-8')).hexdigest()

