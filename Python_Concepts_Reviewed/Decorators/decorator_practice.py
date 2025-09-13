

########################
# EXERCISE 1
########################
# Create a Decorator to Log Function Arguments and Return Value

def printFuncArgs(function):
    def wrapper(*args, **kwargs):
        # Get args
        print(f"For Function {function.__name__} These are the Arguments passed and are in order-> {list(args)}")
        # Get kwargs
        print(f"For Function {function.__name__} These are the Keyowrd Arguments passed -> {kwargs}")
        return function(*args, **kwargs)
    return wrapper

@printFuncArgs
def userSum(user: str, var1: int, var2: int) -> int:
    sum = var1 + var2
    output = f"User -> {user} wants to print sum of two values. The sum is {sum}, For values summed up please check the line above"
    return output


########################
# EXERCISE 2
########################
# Create a Decorator to Measure Function Execution Time

from time import time
import requests

def timed(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        value = function(*args, **kwargs)
        end_time = time()
        print(f"The function -> {function.__name__} ran for {round(end_time - start_time, 1)} seconds")
        return value
    return wrapper

@timed
@printFuncArgs
def predictPersonAgeBasedOnName(name: str):
    response = requests.get(url='https://api.agify.io/', params={"name":name })
    data = response.json()
    return data.get("age")





###############################
# MAIN CODE CALL
###############################
if __name__ == '__main__':

    ## Exercise 1 -> # Create a Decorator to Log Function Arguments and Return Value
    #print(userSum("Arjun", 5, 10))

    ## Exercide 2 -> # Create a Decorator to Measure Function Execution Time
    # print(predictPersonAgeBasedOnName("Rama"))