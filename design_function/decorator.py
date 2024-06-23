def decorate_function(func):
    def warp():
        print("SITCON Camp use function '{}'".format(func.__name__))
        func()
    return warp


@decorate_function
def small_stone():
    print("小石大叫 !!!")

small_stone()