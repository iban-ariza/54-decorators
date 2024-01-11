"""
Create a class User with an authentication decorator.

This module shows how to use parameters in wrapper functions with *args, **kwargs.
We want to have multiple decorators together.
"""

class User:

    def __init__(self, name: str):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    """Decorator function that authenticates for each blog post"""
    def wrapper(*args, **kwargs):
        """
        Wrapper function with additional functionality to existing function.
        The decorated function has to have the same inputs as the existing function (create blog post),
        otherwise it will crash. That is why the args, kwargs.
        Is authenticated is calling -> wrapper(___), which is create_blog_post(user), ...
        """
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated
def create_blog_post(user: User):
    """
    Because this function has a parameter, that needs to be accessed by the wrapper function,
    then we use *args, **kwargs in order to pass that to the wrapper function.
    :param user:
    :return:
    """
    print(f"This is user's {user.name} blog post!")


new_user = User("Iban")
# comment/uncomment to see how to decorator works (only when authenticated, we print the result)
# new_user.is_logged_in = True
create_blog_post(new_user)




