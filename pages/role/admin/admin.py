from main_files.decorator.decorator_func import log_decorator
from pages.role.admin.admin_user_menu import AdminUserMenu


class Admin:
    def __init__(self):
        self.__user_menu = AdminUserMenu()

    # for user menu

    @log_decorator
    def show_all_users(self):
        print("Waiting...")
        self.__user_menu.show_all_users()
        return True

    @log_decorator
    def create_user(self):
        self.__user_menu.create_user()
        return True

    # / for user menu
    @log_decorator
    def create_restaurant(self):
        pass
