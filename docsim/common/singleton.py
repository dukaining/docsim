import threading

def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func

def Singleton(cls):
    instances = {}

    @synchronized
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


'''

if __name__ == '__main__':
    @Singleton
    class Test:
        a = 1
    t1 = Test()
    t2 = Test()
    print(id(t1))
    print(id(t2))

'''