teacher_name = input("What is your name? ")
print(f"\nHello {teacher_name}, Welcome to the Test Scoring System by Andyka")

first_name = input("\nEnter the student First name: ")
middle_name = input("Enter the student Middle name: ")
last_name = input("Enter the student Last name: ")
student_class = input("\nEnter the student class: ")
student_name = first_name + " " + middle_name + " " + last_name

course1 = input("\nEnter the name of Course: ")
course2 = input("Enter the name of Course: ")
course3 = input("Enter the name of Course: ")

score1 = float(input(f"\nEnter the score for {course1} course: "))
score2 = float(input(f"Enter the score for {course2} course: "))
score3 = float(input(f"Enter the score for {course3} course: "))

score_number = [score1, score2, score3]
average_user_score = sum(score_number) / len(score_number)

minimum_score = 8

print(f"\nTest result of {student_name} from Class {student_class}")
print(f"- {course1}: {score1}")
print(f"- {course2}: {score2}")
print(f"- {course3}: {score3}")
print(f"\nThe average score of {student_name} is {average_user_score:.2f}")

if average_user_score < minimum_score:
    print(f"\n{student_name} failed the test!")
else:
    print(f"\n{student_name} passed the test!")
