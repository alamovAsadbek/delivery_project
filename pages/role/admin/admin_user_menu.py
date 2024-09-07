from components.color_text.color_text import print_bold
from components.pagination.pagination import Pagination
from components.random_password.generate_password import generate_password
from components.random_username.generate_username import get_username
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
                role = 'owner'
            else:
                print("Invalid choice")
                continue
            break
        print("Creating an account...")
        if role != 'user':
            username = get_username(table_name='users', name=first_name, key=role)
        else:
            username = get_username(table_name='couriers', name=first_name)
        password = generate_password()
        print(f'{role.capitalize()} username: {print_bold(username, 32)}')

