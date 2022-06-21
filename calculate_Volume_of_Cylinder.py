import math

print("Volume of cylinder calculator")
print("\n\n")

height_of_cylinder = float(input("What is the height of the cylinder: "))
radius_of_cylinder = float(input("What is the radius of the cylinder: "))


def calculator(prompt):
    run_again = True
    while(run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: Value must be a number \n")
        except:

