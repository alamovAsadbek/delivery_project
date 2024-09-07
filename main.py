from main_files.decorator.decorator_func import log_decorator
from pages.auth.auth import Auth


@log_decorator
def auth_menu():
    print('Waiting...')
    auth = Auth()
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
                auth_menu()
            elif result_login['role'] == 'admin':
                pass
        elif user_input == 3:
            pass
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


@log_decorator
def admin_menu():
    pass
