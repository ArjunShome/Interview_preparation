
class ApproxSalary:
    def __init__(self, company_name):
        self.company_name = company_name

    def __call__(self, func):
        def inner(*args, **kwargs):
            print(func(*args, **kwargs))
            self.calc_expected_salary_company(args[0])
        return inner

    def calc_expected_salary_company(self, name_salary_map):
        if self.company_name == "Google":
            multiplier = 1.5
        elif self.company_name == "Microsoft":
            multiplier = 1.7

        output_Str = f"{self.company_name}'s Expected Salary : " 
        for name, salary in name_salary_map.items():
            output_Str += f'{name} -> {int(salary * multiplier)}, '
        print(output_Str)



@ApproxSalary('Google')
def display_Salary(dict_name_salary):
    output_str = "Current Salary : "
    for name, salary in dict_name_salary.items():
            output_str += f'{name} -> {salary}, '
    return output_str


########################## EXERCISE ADVANCED #############################################################
# Create a class decorator that caches the results of a method based on its arguments. 
# If a result for a given set of arguments is already cached, it should be returned directly; otherwise, 
# the method should be executed, and the result cached for future use. Add an expiration time to the cache
##########################################################################################################
import time
class Cached:
    def __init__(self, duration):
        self.duration = duration
        self.result = {}

    def __call__(self, func):
        def inner(*args, **kwargs):
            arg_1 = args[0]
            arg_2 = args[1]

            if (arg_1, arg_2) in self.result:
                res, cache_time = self.result[(arg_1, arg_2)]
                time_diff = time.time() - cache_time
                if time_diff <= self.duration:
                    print("Getting value from Cache")  
                else:
                    self.result.pop((arg_1, arg_2))
                    print("Computing..")
                    res = func(*args, **kwargs)
                    self.result[(arg_1, arg_2)] = (res, time.time())
            else:
                print("Computing..")
                res = func(*args, **kwargs)
                self.result[(arg_1, arg_2)] = (res, time.time())

            print(res)

        return inner
    
# Any values cached should be there for 5 seconds
@Cached(20)
def sum(val_1, val_2):
    return val_1 + val_2


    


if __name__ == "__main__":
    # # Understanding
    # dict_name_salary = {'Arjun': 20000, 'Ayan': 40000,'Ajoy': 50000}
    # display_Salary(dict_name_salary)

    ## EXERCISE CODE
    sum(2, 5)
    time.sleep(2)
    sum(8, 2)
    sum(2, 5)
    print("Sleeoing...")
    time.sleep(8)    
    print("WOKE UP...")
    time.sleep(10)
    sum(2,5)
    sum(8, 2)







# {'Arjun': 20000, 'Ayan': 40000,'Ajoy': 50000}
# current salary : Arjun -> 20000, Ayan -> 40000, Ajoy -> 50000

# Google's expected sary : Arjun -> 1.5x, Ayan -> 1.5x, Ajoy -> 1.5x
# Microsoft's expected salary: Arjun -> 1.7x, Ayan -> 1.7x, Ajoy -> 1.7x
