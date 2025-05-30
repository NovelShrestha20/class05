def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
#calling the function with arbitary keyword arguments

describe_person(name="Novel", age=19, city="Butwal", profession="Student")