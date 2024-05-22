import sympy
from sympy import *
from sympy.calculus.util import continuous_domain

class Linearizer:

    @staticmethod
    def init_symbol(input_variable):
        if input_variable != str(input_variable):
            raise Exception("Must input string to initialize symbol")
        return symbols(input_variable)

    @staticmethod
    def init_function(input_function):
        if input_function != str(input_function):
            raise Exception("Must input string to initialize function")
        expression = sympify(input_function)
        return expression

    @staticmethod
    def domain(input_function):
        x = Linearizer.init_symbol("x")
        domain = continuous_domain(input_function, x, sympy.Reals)
        return domain

    @staticmethod
    def linearize(user_function, a):
        x = Linearizer.init_symbol("x")
        user_function = Linearizer.init_function(user_function)
        a = float(a)

        if a not in Linearizer.domain(user_function):
            a = input("x was not in the domain, try another value: ")
            a = float(a)


        foa = user_function.evalf(subs = {x: a})

        fpoa = user_function.diff(x)
        fpoa = fpoa.evalf(subs = {x: a})

        linearized_function = Linearizer.init_function(f"{foa} + {fpoa} * (x - {a})")
        return linearized_function


user_function = input("Input your function in terms of x -- be aware of how to write different operations: ")
a = input("Input the a input value you would like to create the linearized function [notated L(x)]: ")
linearized_function = Linearizer.linearize(user_function, a)
print("L(x) =", linearized_function, " --> this is the tangent line equation")
print()

str(user_function)
x = Linearizer.init_symbol("x")
user_function = Linearizer.init_function(user_function)
user_val = input("Please enter the number you would like to approximate using the L(x) function: ")

actual_output = user_function.evalf(subs = {x: user_val})
linearized_output = linearized_function.evalf(subs = {x: user_val})
delta = abs(actual_output - linearized_output)

print("Actual output of the function: ", actual_output)
print("Approximated output of the function using tangent lines: ", linearized_output)
print("Difference between actual output and linearized output (absolute value): ", delta)
