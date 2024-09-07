from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminUserMenu:
    @log_decorator
    def get_data(self):
        query = '''
                SELECT * FROM users WHERE ROLE='user'
                '''
        all_users = execute_query(query, fetch='all')
        return all_users

    @log_decorator
    def show_all_users(self):
        all_users = self.get_data()
        if all_users is None:
            print("Users not found")
            return False
        pagination = Pagination(table_name='users', data=all_users,
                                table_keys=['id', 'first_name', 'last_name', 'phone_number', 'role', 'created_at'],
                                display_keys=['ID', 'FIRST_NAME', 'LAST_NAME', 'PHONE_NUMBER', 'ROLE', 'created_at'])
        pagination.page_tab()
        return True
