import hashlib
import threading

from components.color_text.color_text import print_bold
from components.pagination.pagination import Pagination
from components.random_password.generate_password import generate_password
from components.random_username.generate_username import get_username
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
            return None
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
        select * from branch where RESTAURANT_ID=%s
        '''
        params = (get_restaurant['id'],)
        result = execute_query(query, params, fetch='all')
        pagination = Pagination(table_name='branch', data=result,
                                table_keys=['id', 'name', 'username', 'phone_number', 'location'],
                                display_keys=['ID', 'Name', 'Username', 'Phone Number', 'Location'])
        pagination.page_tab()
        return True

    @log_decorator
    def create_branch(self, update_data=None):
        get_restaurant = update_data
        if update_data is None:
            get_restaurant = self.select_restaurant()
        if get_restaurant is None:
            return False
        if update_data is not None:
            print(f"Branch: {get_restaurant['name']}\n")
        else:
            print(f"\nRestaurant: {get_restaurant['name']}\n")
        branch_name = input("Enter branch name: ").strip()
        location = input("Enter location: ").strip()
        print("Creating branch...")
        if update_data is not None:
            username = update_data['username']
        else:
            username = get_username(table_name='branch', name=branch_name, key='filial')
        password = generate_password()
        hash_password = hashlib.sha256(password.__str__().encode('utf-8')).hexdigest()
        print(f"\nBranch username: {print_bold(username, 32)} and branch password: {print_bold(password, 32)}\n")
        if update_data is None:
            query = '''
            INSERT INTO branch(name, location, restaurant_id, password, username, phone_number, role)
             VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
            params = (branch_name, location, get_restaurant['id'], hash_password, username,
                      get_restaurant['phone_number'], 'branch')
        else:
            query = '''
            UPDATE branch SET name=%s, location=%s, password=%s, username=%s, phone_number=%s where id=%s
            '''
            params = (
                branch_name, location, hash_password, username, get_restaurant['phone_number'], get_restaurant['id'],)
        threading.Thread(target=execute_query, args=(query, params)).start()
        if update_data is None:
            print("Branch created!")
        else:
            print("Branch updated!")
        return True

    @log_decorator
    def update_branch(self):
        self.show_all_branches()
        branch_id = int(input("Enter branch ID to update or 0 to exit: ").strip())
        if branch_id == 0:
            print("Exit")
            return False
        query = '''
        SELECT * FROM branch WHERE id=%s
        '''
        params = (branch_id.__str__(),)
        result = execute_query(query, params, fetch='one')
        if result is None:
            print("Branch not found")
            return False
        print(
            f"\nBranch name: {print_bold(result['name'], 34)}\n"
            f"Location: {print_bold(result['location'], 34)}\nUsername: {print_bold(result['username'], 34)}\n"
            f"Phone Number: {print_bold(result['phone_number'], 34)}\n")
        self.create_branch(update_data=result)
        return True

    @log_decorator
    def delete_branch(self):
        self.show_all_branches()
        branch_id = int(input("Enter branch ID to delete or 0 to exit: ").strip())
        if branch_id == 0:
            print("Exit")
            return False
        query = '''
        SELECT * FROM branch b
        INNER JOIN restaurants r on branch.RESTAURANT_ID = r.ID
        WHERE r.owner_id=%s AND b.id=%s
        '''
        params = (self.active_user['id'], branch_id.__str__(),)
        result = execute_query(query, params, fetch='one')
        if result is None:
            print("Branch not found")
            return False
        confirm = input("Are you sure you want to delete this branch? (y/n) ").strip().lower()
        if confirm == 'y':
            query = '''
            DELETE FROM branch b where b.id=%s
            '''
            params = (branch_id.__str__(),)
            threading.Thread(target=execute_query, args=(query, params)).start()
            print("Branch deleted!")
            return True
        elif confirm == 'n':
            print("Exit")
            return False
        else:
            print("Invalid input")
            return False
