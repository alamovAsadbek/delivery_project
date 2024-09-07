from components.pagination.pagination import Pagination
from main_files.decorator.decorator_func import log_decorator


class AdminUserMenu:
    @log_decorator
    def show_all_users(self):
        pagination = Pagination(table_name='users',
                                table_keys=['id', 'first_name', 'last_name', 'phone_number', 'role', 'created_at'],
                                display_keys=['ID', 'FIRST_NAME', 'LAST_NAME', 'PHONE_NUMBER', 'ROLE', 'created_at'])
        pagination.page_tab()
        return True

    @log_decorator
    def create_user(self):
        pass
