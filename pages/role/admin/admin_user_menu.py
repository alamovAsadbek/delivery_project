from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminUserMenu:
    @log_decorator
    def get_data(self):
        query = '''
                SELECT * FROM users
                '''
        all_users = execute_query(query, fetch='all')
        return all_users

    @log_decorator
    def show_all_users(self):
        all_users = self.get_data()
        if all_users is None:
            print("Users not found")
            return False

