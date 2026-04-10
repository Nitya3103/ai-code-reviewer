import os

password = "admin123"  # hardcoded password

def divide(a, b):
    return a / b  # bug: no check for division by zero

def get_user(id):
    query = "SELECT * FROM users WHERE id = " + id  # security issue: SQL injection
    return query

def slow_function(data):
    result = []
    for i in range(len(data)):       # performance issue
        result.append(data[i] * 2)
    return result
