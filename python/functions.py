def sum(x,y):
    return (x+y)
print(sum(4,5))
#default parameter value
def student_names(name="Sarah"):
    print("Hello "+name)
student_names()
student_names("John")
#keyword parameters
def more_num(a,b=7,c=10):
    print("a is",a,"and b is",b,"while c is",c)
more_num(3,7)
more_num(23,c=17)
more_num(c=40,a=80)
#functions returning other functions
def greeting():
    def say_hello():
        return "Hello"
    return say_hello
hello =greeting()
print(hello())
#assigning functions to variables
def mynum(x):
    return x+1
num = mynum
print(num(7))
#global and local variables
x=10
def my_nos(x):
    print(x)
    x=7
    print("my fav no is",x)
my_nos(x)
print(x)
#nesting functions
def mynum(a):
    def num(a):
        return a+1
    result=num(a)
    return result
print(mynum(4))
#nested function accessing variable scope
def display_message(message):
    "hello"
    def message_sender():
        "nested function"
        print(message)
    message_sender()
display_message("Show me money")
#pass statement
def dream_home():
    pass
#passing functions as arguments
def no(b):
    return b+1
def addno(c):
    newno=7
    return c(newno)
print(addno(no))
#VarArgs parameters
def total_num(a=7,*numbers,**phonebook):
    print("my fav no is",a)

    for num in numbers:
        print("num",num)

    for name,phone_num in phonebook.items():
        print(name,phone_num)

total_num(7,1,2,3,Jane=2222,John=4444,Angela=5555)
#anonymous functions
c=lambda d,e:d+e
print(c(7,8))

def ghost_num(n):
    return lambda f:f*n
double_num=ghost_num(2)
print(double_num(20))
#DocStrings
def add_numbers(d,e):
    '''Adding two numbers'''
    print(d,e)
add_numbers(8,4)
print(add_numbers.__doc__)
#decorators
def my_decorator(function):
    def wrapper():
        myfunc=function()
        convert_uppercase=myfunc.upper()
        return convert_uppercase
    return wrapper
def say_hello():
    return "hello world"
decorate=my_decorator(say_hello)
print(decorate())