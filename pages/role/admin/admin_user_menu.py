from components.pagination.pagination import Pagination
from main_files.decorator.decorator_func import log_decorator


class AdminUserMenu:
    def __init__(self):
        pass

    @log_decorator
    def show_all_users(self):
        pagination = Pagination(table_name='users',
                                table_keys=['id', 'first_name', 'last_name', 'phone_number', 'role', 'created_at'],
                                display_keys=['ID', 'FIRST_NAME', 'LAST_NAME', 'PHONE_NUMBER', 'ROLE', 'created_at'])
        pagination.page_tab()
        return True

    @log_decorator
    def create_user(self):
        first_name = input('First Name: ').strip()
        last_name = input('Last Name: ').strip()
        phone_number = input('Phone Number: ').strip()
        role = 'user'
        while True:
            print("\nChoose user role")
            print("1. User\t2. Courier\t3. Owner restaurant")
            user_choice = int(input("Enter your choice: ").strip())
            if user_choice == 1:
                role = 'user'
            elif user_choice == 2:
                role = 'courier'
            elif user_choice == 3:
                role = 'owner_restaurant'
            else:
                print("Invalid choice")
                continue
            break
        print("Creating an account...")
        username = 'user'
