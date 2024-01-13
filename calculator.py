# x = int(input("Type x "))
# y = int(input("Type y "))
# z = x+y
# print(f"{z:,}")

# x = int(input("Type x "))
# y = int(input("Type y "))
# z = x/y
# print(f"{z:.2f}")

# x = int(input("Type x "))
# y = int(input("Type y "))
# z = round(x/y,2)
# print(f"{z}")


def main():
    x = int(input("What is the value of X? "))
    y = int(input("What is the value of Y? "))


    print ("Sum is ", calc(x,y))

def calc(a,b):

    z = a + b
    return z
    
    

main()

