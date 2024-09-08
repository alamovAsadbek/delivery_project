from main_files.decorator.decorator_func import log_decorator
from pages.role.owner.branch import Branch


class OwnerRestaurant:
    def __init__(self):
        self.__branch = Branch()

    @log_decorator
    def show_all_branches(self):
        pass
