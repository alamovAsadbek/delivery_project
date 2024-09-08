from main_files.decorator.decorator_func import log_decorator


class OwnerRestaurantMenu:
    @log_decorator
    def show_all_owner_restaurants(self):
        query='''
        SELECT *
        FROM restaurants
        WHERE OWNER_ID = %s
        '''
        params=()
