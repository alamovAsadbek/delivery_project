from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Tables:
    @log_decorator
    def create_users_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS users (
            ID BIGSERIAL PRIMARY KEY,
            FIRST_NAME VARCHAR(255) NOT NULL,
            LAST_NAME VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            phone_number BIGINT NOT NULL UNIQUE,
            ROLE VARCHAR(255) NOT NULL,
            IS_LOGIN BOOLEAN NOT NULL DEFAULT FALSE,
            CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP        
            )
            '''
        execute_query(query)
        return True

    @log_decorator
    def create_restaurants_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS restaurants (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(255) NOT NULL,
        USERNAME VARCHAR(255) NOT NULL UNIQUE,
        PASSWORD VARCHAR(255) NOT NULL,
        ROLE VARCHAR(255) NOT NULL,
        PHONE_NUMBER BIGINT NOT NULL UNIQUE,
        COMPANY_FEE BIGINT NOT NULL,
        OWNER_ID BIGINT NOT NULL REFERENCES users(ID) ON DELETE CASCADE,
        CREATED_AT TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_branch_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS branch (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(255) NOT NULL,
        LOCATION VARCHAR(255) NOT NULL,
        RESTAURANT_ID BIGINT NOT NULL REFERENCES restaurants(ID) ON DELETE CASCADE,
        PASSWORD VARCHAR(255) NOT NULL,
        USERNAME VARCHAR(255) NOT NULL UNIQUE,
        PHONE_NUMBER BIGINT NOT NULL UNIQUE,
        ROLE VARCHAR(255) NOT NULL,
        CREATED_AT TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_products_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS products (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(255) NOT NULL,
        PRICE BIGINT NOT NULL,
        RESTAURANT_ID BIGINT NOT NULL REFERENCES restaurants(ID) ON DELETE CASCADE,
        STATUS BOOLEAN NOT NULL DEFAULT TRUE,
        CREATED_AT TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_baskets_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS baskets (
        ID BIGSERIAL PRIMARY KEY,
        USER_ID BIGINT NOT NULL REFERENCES users(ID) ON DELETE CASCADE,
        STATUS VARCHAR(255) NOT NULL,
        CREATED_AT TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_basket_items_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS basket_items (
        ID BIGSERIAL PRIMARY KEY,
        BASKET_ID BIGINT NOT NULL REFERENCES baskets(ID) ON DELETE CASCADE,
        PRODUCT_ID BIGINT NOT NULL REFERENCES products(ID) ON DELETE CASCADE,
        QUANTITY BIGINT NOT NULL
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_orders_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS orders (
        ID BIGSERIAL PRIMARY KEY,
        USER_ID BIGINT NOT NULL REFERENCES users(ID) ON DELETE CASCADE,
        STATUS VARCHAR(255) NOT NULL,
        CREATED_AT TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_order_items_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS order_items (
        ID BIGSERIAL PRIMARY KEY,
        ORDER_ID BIGINT NOT NULL REFERENCES orders(ID) ON DELETE CASCADE,
        PRICE BIGINT NOT NULL,
        NAME VARCHAR(255) NOT NULL,
        QUANTITY BIGINT NOT NULL,
        BRANCH_ID BIGINT NOT NULL REFERENCES branch(ID) ON DELETE CASCADE
        )
        '''
        execute_query(query)
        return True
