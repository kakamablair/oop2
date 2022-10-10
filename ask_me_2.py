try:
    name = input("What is your lovely name? ")
    name = name.title()
    print("Hello, " , name)
except ValueError:
    print(" hello, stranger.")

