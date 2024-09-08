from main_files.decorator.decorator_func import log_decorator
from pages.role.admin.admin_restaurant_menu import AdminRestaurantMenu
from pages.role.admin.admin_user_menu import AdminUserMenu


class Admin:
    def __init__(self):
        self.__user_menu = AdminUserMenu()
        self.__restaurant_menu = AdminRestaurantMenu()

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

    @log_decorator
    def update_user(self):
        self.__user_menu.update_user()
        return True

    @log_decorator
    def delete_user(self):
        self.__user_menu.delete_user()
        return True

    # / for user menu

    # for restaurant menu
    @log_decorator
    def show_all_restaurants(self):
        self.__restaurant_menu.show_all_restaurants()
        return True

    @log_decorator
    def create_restaurant(self):
        self.__restaurant_menu.create_restaurant()
        return True

    @log_decorator
    def update_restaurant(self):
        self.__restaurant_menu.update_restaurant()
        return True

    @log_decorator
    def delete_restaurant(self):
        self.__restaurant_menu.delete_restaurant()
        return True
    # / for restaurant menu
