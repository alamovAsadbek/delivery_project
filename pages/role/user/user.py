from components.pagination.pagination import Pagination
from main_files.decorator.decorator_func import log_decorator


class User:
    @log_decorator
    def order_food(self):
        pagination = Pagination(table_name='restaurants', table_keys=['id', 'name'],
                                display_keys=['ID', 'Name'])
        if not pagination.page_tab():
            return False
