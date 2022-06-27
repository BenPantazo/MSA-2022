#print the menu



print("Select option from Menu\n-----------------------")
print("1. Login")
print("2. Create User")
while True:
    user_option = input("Would you like to (1) Login or (2) Create an account? ")
    if user_option != '1' and user_option != '2':
        print("\nERROR: Enter a 1 or 2")
        continue
    else:
        print("YaY! Good input")
        break     


if user_option == "1":
    while True:
        #If user chose 1, ask for user name and password and
        user_name = input("Please enter your user name: ")
        user_pass = input("Please enter your password: ")
        # - validate username and password combination in the users.txt file
        #open the users files
        user_file = open("users.txt", "r")
        user_found = False

        #read the lines from the file
        for line in user_file:
            credentials = line.split(", ")
             #compare username and password for a match
            if user_name == credentials[0] and user_pass == credentials[1].rstrip():
                user_found = True
                break

        if user_found:
            # - if valid then move on to prompt for student data
            print(f"User {user_name} successfully logged in!\n")
            break
        else:
            # - if not valid combination reprompt the user. 
            print(f"User {user_name} not found!\n")
elif user_option == "2":
    run_again = True
    while (run_again):
        user_name = input("Please enter your user name (4 - 12) characters: ")
        user_pass = input("Please enter your password (6 - 16) characters: ")
        user_name_length = len(user_name)
        password_length = len(user_pass)
        if (user_name_length >= 6 and user_name_length <= 12 and password_length >= 6 and password_length <= 16):
            user_file = open("users.txt", "a")
            user_file.write(f"{user_name}, {user_pass}\n")
            user_file.close()
            print("\nSuccessful Login")
            run_again = False
        else:
            print("ERROR: Incorrect Username or Password length")
            continue
student_names = []
student_scores = []
student_letter_grade = []

number_of_students = int(input("Enter number of students to enter grades for: "))

for counter in range(number_of_students):
    student_name = input("Enter Student name: ")
    student_score = float(input("Enter student score: "))
    student_names.append(student_name)
    student_scores.append(student_score)
    if student_score >= 90 and student_score <= 100:
        student_letter_grade.append("A")
    elif student_score >= 80 and student_score <= 89:
        student_letter_grade.append("B")
    elif student_score >= 70 and student_score <= 79:
        student_letter_grade.append("C")
    elif student_score >= 60 and student_score <= 69:
        student_letter_grade.append("D")
    else:
        student_letter_grade.append("F")


for index in range(len(student_names)):
    print(f"{student_names[index]} : {student_scores[index]} : {student_letter_grade[index]} ")





