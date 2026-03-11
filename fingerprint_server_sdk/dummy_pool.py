class DummyAsyncResult:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


class DummyPool:
    def apply_async(self, func, args=(), kwds={}, callback=None):
        result = func(*args, **kwds)
        if callback is not None:
            callback(result)
        return DummyAsyncResult(result)

    def close(self):
        pass

    def join(self):
        pass
