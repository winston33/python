def x(s):
    print("Hello, " + s +"!")
x("lox")
x("mudak")
x("pitr")

def print_percents(x,y):
    """What percentage of x is y"""
    print(str(y) + " is " + str(percents(x,y))+ "% of " + str(x))

def percents(x,y):
    """What percentage of x is y"""
    return (y/x*100)

percents(200,50)
print_percents(200,5)
print_percents(200,50)
