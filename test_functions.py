args1 = []
kwargs1 = {}
a = 4
b = True
c = "hello"
d = 'c'
# Uses global values
def func1():
    a += 1
    b = True and b
    c = c + " there"

args2 = []
kwargs2 = {}
def helper():
    print("helper")
    return True

# Makes external function calls
def func2():
    helper() 

args3 = []
kwargs3 = {}
def func3():
    pass

args4 = []
kwargs4 = {}
def func4():
    pass
