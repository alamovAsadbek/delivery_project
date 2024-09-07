from components.pagination.pagination import Pagination
from main_files.decorator.decorator_func import log_decorator


class AdminUserMenu:
    def __init__(self):
        self.__user_pagination = Pagination()

    @log_decorator
    def show_all_users(self):
        all_users = self.get_data()
        if all_users is None:
            print("Users not found")
            return False
