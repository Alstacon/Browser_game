class BaseSingleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(BaseSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

