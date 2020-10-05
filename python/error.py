#print(x)
try:
    print(x)
except:
    print("Variable is not defined")
else:
    print("Hello")
finally:
    print("you may get an error if no variable is specified")

#another way

while True:
    try:
        n=int(input("Enter an integer"))
        break
    except ValueError:
        print("No valid integer entered")
print("Great you have entered an integer")

#c=12/0
try:
    n=12/int(input("Enter a natural no."))
    print("the value of your no. is",n)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print("Hope you entered a valid no.")