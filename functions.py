# def hello(to = "World"):
#     print("Hello ", to)

# hello()
# name = input("Whats your name?")
# hello(name)

def main():
    name = input("Whats your name?")
    name = name.title()
    hello()
    hello(name)



def hello(to = "World"):
    print("Hello ", to)

main()
