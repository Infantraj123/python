from ex1 import add_student, display_students

# Get the number of students as input
num_students = int(input("Enter Number of Students: "))

# For each student
for i in range(1, num_students + 1):
    print(f"Enter Details of Student {i}:")
    reg_no = input("Enter Student Reg. No.: ")
    name = input("Enter Student Name: ")
    marks = list(map(int, input("Enter Marks separated by spaces: ").split()))
    add_student(reg_no, name, marks)

# Get input to display details
display_option = input("How to display Student Details (All/Specific): ").upper()

if display_option == 'ALL':
    display_students()
else:
    register_no = input("Enter Register Number: ")
    display_students(register_no)
