from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminUserMenu:
    @log_decorator
    def get_data(self):
        pass

    @log_decorator
    def show_all_users(self):
        query = '''
        SELECT * FROM users
        '''
        all_users = execute_query(query, fetch='all')
        print(all_users)
