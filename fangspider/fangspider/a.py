def log(func):
    def chu(*args,**kwargs):
        print('call %s'%(func.__name__))
        return func(*args,**kwargs)
    return chu

@log
def now():
    print('输出')

now()