import threading

from main_files.decorator.decorator_func import log_decorator
from pages.auth.auth import Auth
from pages.role.admin.admin import Admin
from pages.role.owner.owner import OwnerRestaurant


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
            auth.register()
        elif user_input == 2:
            result_login = auth.login()
            if not result_login['is_login']:
                print('Login failed')
                auth_menu()
            elif result_login['role'] == 'admin':
                admin_menu()
            elif result_login['role'] == 'user':
                user_menu()
            elif result_login['role'] == 'courier':
                courier_menu()
            elif result_login['role'] == 'restaurant':
                restaurant_menu()
            elif result_login['role'] == 'branch':
                branch_menu()
            elif result_login['role'] == 'owner':
                owner_restaurant_menu()
            else:
                print("Login failed")
                auth_menu()
        elif user_input == 3:
            print('Good bye!')
            auth.logout()
            return
        auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


# admin menu
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
            admin_restaurants_menu()
        elif user_input == 2:
            admin_users_menu()
        elif user_input == 3:
            print('Exit')
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()


@log_decorator
def admin_restaurants_menu():
    print("Waiting...")
    admin = Admin()
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
            admin.create_restaurant()
        elif user_input == 2:
            admin.update_restaurant()
        elif user_input == 3:
            admin.delete_restaurant()
        elif user_input == 4:
            admin.show_all_restaurants()
        elif user_input == 5:
            return admin_menu()
        else:
            print("Wrong input")
        admin_restaurants_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_restaurants_menu()


@log_decorator
def admin_users_menu():
    print("Waiting...")
    admin = Admin()
    text = '''
1. Create User
2. Update User
3. Delete User
4. Show all Users
5. Back
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: ').strip())
        if user_input == 1:
            admin.create_user()
        elif user_input == 2:
            admin.update_user()
        elif user_input == 3:
            admin.delete_user()
        elif user_input == 4:
            admin.show_all_users()
        elif user_input == 5:
            admin_menu()
        else:
            print('Wrong input')
        admin_users_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_users_menu()


# / admin menu

# user menu
@log_decorator
def user_menu():
    text = '''
1. Foods
2. My orders
3. Basket
4. Logout
    '''
    print(text)
    try:
        user_input = int(input("Choose menu: "))
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            threading.Thread(target=auth.logout).start()
            print("Logged out")
            auth_menu()
        else:
            print("Wrong input")
            user_menu()
    except Exception as e:
        print(f'Error: {e}')
        user_menu()


# /user menu

# restaurant menu
@log_decorator
def restaurant_menu():
    pass


# /restaurant menu

# branch menu
@log_decorator
def branch_menu():
    pass


# /branch menu

# owner restaurant
@log_decorator
def owner_restaurant_menu():
    print("Waiting...")
    owner = OwnerRestaurant()
    text = '''
1. My restaurants
2. Branch
3. Logout
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            owner.show_my_restaurants()
        elif user_input == 2:
            owner_branch_menu()
        elif user_input == 3:
            print("Logout")
            threading.Thread(target=auth.logout).start()
            return auth_menu()
        else:
            print("Wrong input")
        owner_restaurant_menu()
    except Exception as e:
        print(f'Error: {e}')
        owner_restaurant_menu()


@log_decorator
def owner_branch_menu():
    print("Waiting...")
    owner = OwnerRestaurant()
    text = '''
1. Create branch
2. Update branch
3. Delete branch
4. Show all branches
5. Back
    '''
    print(text)
    try:
        user_input = int(input('Choose menu: '))
        if user_input == 1:
            owner.create_branch()
        elif user_input == 2:
            owner.update_branch()
        elif user_input == 3:
            owner.delete_branch()
        elif user_input == 4:
            owner.show_all_branches()
        elif user_input == 5:
            return owner_restaurant_menu()
        else:
            print("Wrong input")
        owner_branch_menu()
    except Exception as e:
        print(f'Error: {e}')
        owner_branch_menu()


# / owner restaurant

# courier menu
@log_decorator
def courier_menu():
    print("Courier menu")
    pass


# /courier menu

if __name__ == '__main__':
    print('Waiting...')
    auth = Auth()
    auth.logout()
    auth_menu()
