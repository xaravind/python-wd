def add(*args):
    """Function to add any number of arguments."""
    return sum(args)
 
print(add(1,2,3,4,5,6,7,8,9,10,25,30))
 

def user_info(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="vishwas",city="pune",country="India")
