import time


def speed_calc_decorator(speed_function):
    """
    The decorator function gives the name to the decorator.
    The actual addition of functionality happens at the wrapper funtion.
    The wrapper function wraps/adds functionality to the previous existing function.
    """
    def wrapper_function():
        """
        The wrapper/add functionality function wraps the speed_function (existing function) with
        new functionality (calculating the time it takes for the speed_function to run).
        You can also alter what the speed_function returns without the need of modifying it. In this example,
        we return the elapsed time, even though the speed_function might return something else.
        :return:
        """
        pre_time = time.time()
        speed_function()
        post_time = time.time()
        print(f"Difference: {post_time - pre_time}")

        # the speed_function now returns a new value (post_time - pre_time)

        return post_time - pre_time

    # key line - it returns the new wrapped function for execution
    return wrapper_function


@speed_calc_decorator   # decorator (added functionality to fast_function)
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


# returns the post_time - pre_time (because we have added/wrapped functionality to the fast_function)
# and that wrapped functionality includes a different return value.
print(fast_function())
print(slow_function())
