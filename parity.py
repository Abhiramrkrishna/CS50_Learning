def main():
    x = int(input('Whats the value of x?'))

    if is_even(x):
        print('Even')
    else:
            print('Odd')

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

# another method
# return n % 2 == 0 

main()
