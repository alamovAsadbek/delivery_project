from main_files.decorator.decorator_func import log_decorator


@log_decorator
def print_bold(text, color_code):
    BOLD = '\033[1m'
    RESET = '\033[0m'
    color = f'\033[{color_code}m'
    return f"{BOLD}{color}{text}{RESET}"
