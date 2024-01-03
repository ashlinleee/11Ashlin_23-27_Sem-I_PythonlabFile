def details(*args, **kwargs):
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    age = int(input("Enter Age: "))

    print("Additional Details:")
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
details("Additional Arg1", "Additional Arg2", additional_kwarg="Additional KWarg")

