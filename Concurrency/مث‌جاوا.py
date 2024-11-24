from threading import Thread, Lock


def synchronized(func):
    lock = Lock()
    def wrapper(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)
    return wrapper



