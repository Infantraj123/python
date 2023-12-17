students_list = []

def add_student(reg_no, name, marks):
    stud_directory = {'Reg No.': reg_no, 'Name': name, 'Marks': marks}
    students_list.append(stud_directory)
    print(f"Added {name} marks into the List")

def calculate_marks(student_marks):
    total_marks = sum(student_marks)
    average_marks = total_marks / len(student_marks)

    if average_marks >= 90:
        grade = 'A'
    elif 80 <= average_marks <= 89:
        grade = 'B'
    elif 70 <= average_marks <= 79:
        grade = 'C'
    elif 60 <= average_marks <= 69:
        grade = 'D'
    else:
        grade = 'NG'

    return total_marks, average_marks, grade

def display_students(register_no='ALL'):
    print("Student Mark List - I MCom – Semester 1 (2023-24)")
    print("{:<15} {:<20} {:<10} {:<10} {:<10}".format("RegNo", "Name", "Total", "Average", "Grade"))
    
    if register_no == 'ALL':
        for student in students_list:
            total, average, grade = calculate_marks(student['Marks'])
            print("{:<15} {:<20} {:<10} {:<10} {:<10}".format(student['Reg No.'], student['Name'], total, average, grade))
    else:
        for student in students_list:
            if student['Reg No.'] == register_no:
                total, average, grade = calculate_marks(student['Marks'])
                print("{:<15} {:<20} {:<10} {:<10} {:<10}".format(student['Reg No.'], student['Name'], total, average, grade))
