
class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invoked = None
        self.calls = {}

    def __getattr__(self, name):
        if hasattr(self._obj, name):
            self.last_invoked = name
            self.calls[name] = self.calls.get(name, 0)  + 1
            return (getattr(self._obj, name))
        else:
            raise Exception("No Such Method")

    def last_invoked_method(self):
        if self.last_invoked:
            return(str(self.last_invoked))
        else:
            raise Exception("No Method Is Invoked")
        
    def count_of_calls(self, method_name):
        if method_name in self.calls:
            res = self.calls[method_name]
        else:
            res = 0
        return(res)


    def was_called(self, method_name):
        res = bool()
        if method_name in self.calls:
            if self.calls[method_name] == 0:
                res = False
            else:
                res = True 
        else:
            res = False
        return(res)



