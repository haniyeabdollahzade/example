GREETING = "Hello, {name}! You are {age} years old."


def create_greeting(name, age):
    message = GREETING.format(name=name, age=age)
    return message

print(create_greeting('Alice', 30))
print(create_greeting('Bob', 22))