


def comethod(func):

    class wrapper(object):

        def __init__(self, iterator):
            self.__iterator = iterator
            self.__iterator.send(None)
            self.__done = False

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is None and not self.__done:
                self.finish()

        def add(self, value):
            return self.__iterator.send(value)

        __call__ = add

        def finish(self):
            try:
                self.__iterator.send(None)
            except StopIteration:
                self.__done = True
                return True
            return False

    def wrapped(*args, **kwargs):
        return wrapper(func(*args, **kwargs))

    return wrapped
