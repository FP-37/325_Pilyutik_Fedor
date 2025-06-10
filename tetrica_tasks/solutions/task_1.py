"""
Необходимо реализовать декоратор @strict
Декоратор проверяет соответствие типов переданных в вызов функции аргументов типам аргументов,
объявленным в прототипе функции.
(подсказка: аннотации типов аргументов можно получить из атрибута объекта функции func.__annotations__
или с помощью модуля inspect)
При несоответствии типов бросать исключение TypeError
Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str
Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию
"""
import inspect

def strict(func):
    def wrapper(*args, **kwargs):
        # Получаем сигнатуру функции
        sig = inspect.signature(func)
        # Преобразуем позиционные и именованные аргументы в словарь {имя: значение}
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        # Получаем аннотации типов
        annotations = func.__annotations__

        for name, value in bound.arguments.items():
            if name in annotations:
                expected_type = annotations[name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{name}' must be of type {expected_type.__name__}, "
                        f"got {type(value).__name__}"
                    )
        return func(*args, **kwargs)

    return wrapper
