from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query, get_active_user
from main_files.decorator.decorator_func import log_decorator
from pages.role.owner.owner_restaurant_menu import OwnerRestaurantMenu


class Branch:
    def __init__(self):
        self.active_user = get_active_user()
        self.__restaurant_menu = OwnerRestaurantMenu()

    @log_decorator
    def show_all_branches(self):
        print("Waiting...")
        query = '''
        SELECT * FROM branch
        '''
        result_get = execute_query(query)
        pagination = Pagination(table_name='branch', data=result_get,
                                table_keys=['id', 'name', 'username', 'phone_number', 'location'],
                                display_keys=['ID', 'Name', 'Username', 'Phone Number', 'Location'])
        if not pagination.page_tab():
            return False
        return True

    @log_decorator
    def create_branch(self):
        pass
