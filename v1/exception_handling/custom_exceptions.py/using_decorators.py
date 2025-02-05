def handle_error(func):

    def internal_wrapper(*args, **kwargs):

        return func(*args, **kwargs)
    
    return internal_wrapper


# @handle_error
# def divide
    