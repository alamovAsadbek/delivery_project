from main_files.decorator.decorator_func import log_decorator


class Admin:
    @log_decorator
    def create_restaurant(self):
        pass
    print('owner_restaurant')
