password = "admin123"

def divide(a, b):
    return a / b

def get_user(id):
    query = "SELECT * FROM users WHERE id = " + id
    return query
