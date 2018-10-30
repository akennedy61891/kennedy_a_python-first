def greetings ():
    print ("Hello from the greetings function")


# the greetings function just says hello
# invoke or call the function 
greetings()


def greetingsWithArgs(msg="a default message"):
    #make sure definition is same as print statement "msg"
    print("now we're saying", msg, "from another function")


greetingsWithArgs()
greetingsWithArgs("Something new")
greetingsWithArgs("running yet again")

#variables and scope
myNumberVariable = 10


# returning values fro mfunctions (very powerufl)
def someMath(num1=2, num2=4):
    global myNumberVariable

    myNumberVariable = num1 + num2
    return num1 + num2


sum = someMath()
print("we are doing some math and getting", sum)

sum = someMath(10,15)
print("another math operation with", sum, "as the result")

