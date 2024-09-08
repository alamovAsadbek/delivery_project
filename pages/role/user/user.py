from main_files.decorator.decorator_func import log_decorator


class User:
    @log_decorator
    def order_food(self):
        query='''
        select * from restaurants
        '''
