import math
def add(first_number, second_number):
        return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    try:
        return first_number /   second_number
    except ZeroDivisionError:
        return "Error: Division by zero"

def power(first_number, second_number):
    return first_number ** second_number

def angle_to_radians(angle):
    return math.radians(angle)

def sine(angle):
    return math.sin(angle)

def cosine(angle):
    return math.cos(angle)

def tangent(angle):
    return math.tan(angle)

def cotangent(angle):
    return 1 / math.tan(angle)


def natural_log(number):
    return math.log(number)

def log_base_10(number):
    return math.log10(number)

def log_custom_base(number, base):
    return math.log(number, base)