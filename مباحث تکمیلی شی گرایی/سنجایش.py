def decorator_builder(validator):
    def decorator(cal):
        def detail(*nums, **kwargs):
            if validator(*nums, **kwargs):
                return(cal(*nums, **kwargs))
            else:
                return("error")
        return detail
    return decorator
