

class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function
        


def transform_exceptions(func_ls):
    error_ls = list()
    for func in func_ls:
        try:
            func()
            error_ls.append(ExceptionProxy("ok!", func))
        except Exception as e:
            error_ls.append(ExceptionProxy(str(e), func))
    return error_ls
            
    
def f():
    1/0
    # print("here f")

def g():
    print("here g")

tr_ls = transform_exceptions([f, g])

for tr in tr_ls:
    print("msg: " + tr.msg + "\nfunction name: " , tr.function.__name__)
