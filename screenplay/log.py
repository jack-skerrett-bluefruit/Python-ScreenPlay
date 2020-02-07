import functools


class _LogIndent:
    indent_size = 2
    current_indent = indent_size * 2

    @classmethod
    def increase_indent(cls):
        cls.current_indent  = cls.current_indent + cls.indent_size

    @classmethod
    def decrease_indent(cls):
        if cls.current_indent > cls.indent_size:
            cls.current_indent  = cls.current_indent - cls.indent_size

    @classmethod
    def indent(cls) -> str:
        return ' ' * cls.current_indent


def log_message(message: str):
    def decorator_log_message(func):
        @functools.wraps(func)
        def wrapper_log_message(*args, **kwargs):
            print(_LogIndent.indent(), message.format(self=args[0]), sep='')
            value = func(*args, **kwargs)
            return value
        return wrapper_log_message
    return decorator_log_message

