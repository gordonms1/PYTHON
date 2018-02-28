x = 6

# def example():
#     global x
#     print(x)
#     x+=5
#     print(x)
# example()

def example():
    globx=x
    print(globx)
    globx+=5
    print(globx)

    return globx

x = example()
