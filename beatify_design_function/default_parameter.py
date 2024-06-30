def greeting(name:str,greeting:str="Hello"):
    return f"{name}:{greeting}"
print(greeting("Mary"))
print(greeting("Tim","Good to see you"))