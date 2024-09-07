from main_files.decorator.decorator_func import log_decorator


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
            pass
        elif user_input == 3:
            pass
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()
