from main_files.decorator.decorator_func import log_decorator


class OwnerRestaurant:
    def __init__(self):
        pass

    @log_decorator
    def show_all_branches(self):
        pass
