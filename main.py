from main_files.decorator.decorator_func import log_decorator
from pages.auth.auth import Auth


@log_decorator
def auth_menu():
    text = '''
1. Register 
2. Login    
3. Logout
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: ').strip())
        if user_input == 1:
            pass
        elif user_input == 2:
            result_login = auth.login()
            if not result_login['is_login']:
                print('Login failed')
                auth_menu()
            elif result_login['role'] == 'admin':
                return admin_menu()

        elif user_input == 3:
            pass
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


@log_decorator
def admin_menu():
    text = '''
1. Restaurants
2. Users
3. Logout
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: ').strip())
        if user_input == 1:
            return admin_restaurants_menu()
        elif user_input == 2:
            pass
        elif user_input == 3:
            print('Exit')
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()


@log_decorator
def admin_restaurants_menu():
    text = '''
1. Create Restaurant
2. Update Restaurant
3. Delete Restaurant
4. Show all Restaurants
5. Back
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: ').strip())
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            return admin_menu()
        else:
            print("Wrong input")
            return admin_restaurants_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_restaurants_menu()


@log_decorator
def admin_users_menu():
    text = '''
1. Create User
2. Update User
3. Delete User
4. Show all Users
5. Back
    '''
    print(text)


if __name__ == '__main__':
    print('Waiting...')
    auth = Auth()
    auth.logout()
    auth_menu()
