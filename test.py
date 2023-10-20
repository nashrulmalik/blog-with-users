def greeting(*args):
    def hello():
        return "Hello, " + args[0] + "!"
    return hello


greet = greeting("Atlantis")
print(greet())