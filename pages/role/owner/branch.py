from main_files.database.db_setting import execute_query, get_active_user
from main_files.decorator.decorator_func import log_decorator
from pages.role.owner.owner_restaurant_menu import OwnerRestaurantMenu


class Branch:
    def __init__(self):
        self.active_user = get_active_user()
        self.__restaurant_menu = OwnerRestaurantMenu()

    @log_decorator
    def select_restaurant(self):
        self.__restaurant_menu.show_all_owner_restaurants()
        restaurant_id: int = int(input("Enter restaurant ID or enter 0 to exit: ").strip())
        if restaurant_id == 0:
            print("Exit")
            return False
        print("Waiting...")
        query = '''
        SELECT * FROM RESTAURANTS WHERE OWNER_ID=%s and ID=%s
        '''
        params = (self.active_user['id'], restaurant_id.__str__(),)
        result = execute_query(query, params, fetch='one')
        if result is None:
            print("Restaurant not found")
            return None
        return result

    @log_decorator
    def show_all_branches(self):
        print("Waiting...")
        get_restaurant = self.select_restaurant()
        if get_restaurant is None:
            return False
        print(f"\nRestaurant: {get_restaurant['name']}\n")
        query = '''
        SELECT * FROM branch WHERE restaurant_id=%s
        '''
        params = (get_restaurant['id'])
        result = execute_query(query, params, fetch='one')
        print(result)

    @log_decorator
    def create_branch(self):
        pass
