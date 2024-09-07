from main_files.decorator.decorator_func import log_decorator


class Admin:
    @log_decorator
    def show_all_users(self):
        pass

    @log_decorator
    def create_restaurant(self):
        pass
