
import math

print("Volume of cylinder calculator")
print("\n\n")

def calculator(prompt):
    run_again = True
    while(run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: Value must be a number \n")
                continue
        except:
              print("ERROR: Input must be a number.\n")
        else:
            run_again = False
    return user_input


do_again = True
while do_again:
    height_of_cylinder = calculator("What is the height of the cylinder: ")
    radius_of_cylinder = calculator("What is the radius of the cylinder: ")

    area_of_circle = math.pi * radius_of_cylinder**2
    volume_of_cylinder = area_of_circle * height_of_cylinder

    print("Report")
    print("------\n")
    print(f"Volume of Cylinder: {volume_of_cylinder:.2f}")

    re_run = input("would you like to perform another calculation (y/n)? ")
    if re_run == "n":
        print("Thank you for your time!")
        do_again = False





