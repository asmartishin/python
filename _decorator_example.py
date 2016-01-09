#!/usr/bin/env python3

def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Я - код, который работает до вызова функции")
        a_function_to_decorate()
        print("А я - код, срабатывающий после")
    return the_wrapper_around_the_original_function

@my_shiny_new_decorator
def a_stand_alone_function():
    print("Я простая одинокая функция")

a_stand_alone_function()


def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper

@bread
@ingredients
def sandwich(food = "--ветчина--"):
    print(food)

sandwich()
