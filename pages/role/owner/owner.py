from main_files.decorator.decorator_func import log_decorator


class OwnerRestaurant:
    @log_decorator
    def show_all_branches(self):
        pass
