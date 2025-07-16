# Random Testing of concepts

# Generators
def foo():
    yield 10
    yield 20
    yield 30

if __name__ == "__main__":  
    m = foo()
    # print(next(m))  
    # print(next(m))  
    # print(next(m))  
    
    # print(next(m))  # Give an error

    for i in range(3):
        print(m.__iter__)