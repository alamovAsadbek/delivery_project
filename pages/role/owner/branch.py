from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Branch:
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
