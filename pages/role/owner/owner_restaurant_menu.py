from components.pagination.pagination import Pagination
from main_files.database.db_setting import get_active_user, execute_query
from main_files.decorator.decorator_func import log_decorator


class OwnerRestaurantMenu:
    def __init__(self):
        self.active_user = get_active_user()

    @log_decorator
    def show_all_owner_restaurants(self):
        query = '''
        SELECT *
        FROM restaurants
        WHERE OWNER_ID = %s
        '''
        params = (self.active_user['id'],)
        result = execute_query(query, params, fetch='all')
        if result is None:
            print('No owner restaurants found.')
            return False
        pagination = Pagination(table_name='restaurants', data=result,
                                table_keys=['id', 'name', 'username', 'phone_number', 'company_fee', 'created_at'],
                                display_keys=['ID', 'Name', 'Username', 'Phone number', 'Company fee (%) ', 'Created'])
        pagination.page_tab()
        return True
