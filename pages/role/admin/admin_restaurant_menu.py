from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminRestaurantMenu:
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
        pass
