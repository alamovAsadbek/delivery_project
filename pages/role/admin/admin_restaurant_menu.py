from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminRestaurantMenu:
    def __init__(self):
        pass

    @log_decorator
    def show_all_restaurants(self):
        print("Waiting...")
        query = '''
        SELECT * FROM restaurants
        INNER JOIN users u on restaurants.OWNER_ID = u.ID
        '''
        result = execute_query(query, fetch='all')
        print(result)

    @log_decorator
    def create_restaurant(self):
        name = input("Enter restaurant name: ").strip()
        phone_number = int(input("Enter phone number ( +998 ): ").strip())
        company_fee = int(input("Enter company fee (0-100): ").strip())
        query = '''
        SELECT * FROM users
        WHERE role='owner'
        '''
        result = execute_query(query, fetch='all')
        pagination = Pagination(table_name='users', data=result,
                                table_keys=['id, first_name', 'last_name', 'username', 'phone_number'],
                                display_keys=['ID', 'FIRST NAME', 'LAST NAME', 'USERNAME', 'PHONE NUMBER'])
        if not pagination.page_tab():
            pass
