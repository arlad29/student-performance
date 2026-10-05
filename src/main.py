from student import Student

student = Student("Rahul", 101, [80, 90, 70])

percentage = student.calculate_percentage()

grade_points = [8, 9, 7]
cgpa = student.calculate_cgpa(grade_points)

print("Student Name:", student.name)
print("Roll Number:", student.roll_no)
print("Percentage:", percentage)
print("CGPA:", cgpa)
