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


class Log:
    output_messages_to_level = 0
    _current_level = 0
    current_actor = None

    @classmethod
    def to_actions(cls):
        cls.output_messages_to_level = 1

    @classmethod
    def to_tasks(cls):
        cls.output_messages_to_level = 2

    @classmethod
    def increment_level(cls):
        cls._current_level = cls._current_level + 1
        _LogIndent.increase_indent()

    @classmethod
    def decrement_level(cls):
        if cls._current_level > 0:
            cls._current_level = cls._current_level - 1
            _LogIndent.decrease_indent()

    @classmethod
    def should_log(cls):
        return cls._current_level <= cls.output_messages_to_level


def log_message(message: str):
    def decorator_log_message(func):
        @functools.wraps(func)
        def wrapper_log_message(*args, **kwargs):
            if Log.should_log():
                print(_LogIndent.indent(), message.format(self=args[0]), sep='')
            value = func(*args, **kwargs)
            return value
        return wrapper_log_message
    return decorator_log_message

