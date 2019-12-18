def decorator_function(main_function):
    def wrapper_function(*args, **kwargs):              # we are passing args and kwargs so that the function can be passed with arguments
        print('Wrapper executed this before the {}'.format(main_function.__name__))
        return main_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    # This is equivalent to the following:
    # display = decorator_function(display)
    print("display function running")


@decorator_function
def display_info(name, age):
    print("display_info ran with the arguments {} and {}".format(name, age))


display_info("das", 23)

display()


"""The same thing can be done with a class, We can decorate a class and pass the function in that"""

class decorator_class(object):

    def __init__(self, main_function):
        self.main_function = main_function

    def __call__(self, *args, **kwargs):
        print('Call method executed this before the {}'.format(self.main_function.__name__))
        return self.main_function(*args, **kwargs)

@decorator_class
def display():
    # This is equivalent to the following:
    # display = decorator_function(display)
    print("display function running")


@decorator_class
def display_info(name, age):
    print("display_info ran with the arguments {} and {}".format(name, age))


display_info("das", 23)

display()
