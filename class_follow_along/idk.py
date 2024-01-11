def prompt():
    '''Prompt the user to give name and gender. Then displays a welcome message. '''
    name = input("What is your last name?: ")
    gender = input("Are you male or female?: ")
    # return ("Mr." if gender == "m" else "mrs." ) + name
    if gender == "M":
        print(f"Hello, Mr. {name}")
    else:
        print(f"Hello, Ms. {name}")

def age_calc():
    year = int(input("What year were you born?: "))
    age = 2023 - year

    # age = 2023 - int(input("What year were your born?")) 
    return age

