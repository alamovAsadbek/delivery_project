from main_files.decorator.decorator_func import log_decorator
from pages.role.owner.branch import Branch
from pages.role.owner.owner_restaurant_menu import OwnerRestaurantMenu


class OwnerRestaurant:
    def __init__(self):
        self.__branch = Branch()
        self.__restaurant = OwnerRestaurantMenu()

    @log_decorator
    def show_all_branches(self):
        self.__branch.show_all_branches()
        return True

    @log_decorator
    def show_my_restaurants(self):
        self.__restaurant.show_all_owner_restaurants()
        return True
