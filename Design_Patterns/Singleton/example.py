

class Singleton:
    _isinstance = None

    def __new__(cls):
        if not cls._isinstance:
            cls._isinstance=super().__init__(cls)
        return cls._isinstance

class NonSingleton:
    pass

if __name__=="__main__":
    s1=Singleton()
    s2=Singleton()

    ns1 = NonSingleton()
    ns2 = NonSingleton()

    if id(s1)==id(s2):
        print("Class Singleton works, both variables contain the same instance.")
    else:
        print("Class Singleton failed, variables contain different instances.")

    if ns1 == ns2:
        print("Class Singleton Failed, both variables contain the same instance.")
    else:
        print("Class NonSingleton works, variables contain different instances.")