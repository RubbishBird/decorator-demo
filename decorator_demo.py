# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self,lie):
#         lie = lie - 3
#         # print(lie)
#         return method_to_decorate(self,lie)
#     return wrapper
#
# class Lucy(object):
#     def __init__(self):
#         self.age = 32
#     @method_friendly_decorator
#     def sayYourAge(self,lie):
#         print("i am %s, what did you think?" % (self.age + lie))
#
# if __name__ == '__main__':
#
#     i = Lucy()
#     i.sayYourAge(-3)

# ------------------------------------------------------demo1

# def a_decoratoe_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1,arg2):
#         print("i got args! Look:", arg1,arg2)
#         function_to_decorate(arg1,arg2)
#     return a_wrapper_accepting_arguments
#
# @a_decoratoe_passing_arguments
# def print_full_name(first_name,last_name):
#     print("my name is", first_name, last_name)
#
#
# print_full_name("james","kobe")

# ------------------------------------------------------demo2
import time

# def foo():
#     start = time.clock()
#     print("in foo()")
#     end = time.clock()
#     print("time elapsed: " ,(end -start))
# foo()

# ------------------------------------------------------demo3
# import time

# def foo():
#     print("in foo()")
#
# def timeit(func):
#
#     def wrapper():
#         start = time.clock()
#         func()
#         end = time.clock()
#         print("time elapsed: ", (end - start))
#     return wrapper
#
# timeit(foo)


# def func_args(pre='xiaoqiang'):
#     def w_test_log(func):
#         def inner():
#             print('...记录日志...visitor is %s' % pre)
#             func()
#
#         return inner
#
#     return w_test_log
#
#
# # 带有参数的修饰器能够起到在运行时，有不同的功能
#
# # 先执行func_args('wangcai')，返回w_test_log函数的引用
# # @w_test_log
# # 使用@w_test_log对test_log进行修饰
# @func_args('wangcai')
# def test_log():
#     print('this is test log')
#
# test_log()

# ------------------------------------




