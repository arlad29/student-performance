from src.student import Student


def test_calculate_percentage():
    student = Student("Rahul", 101, [80, 90, 70])

    assert student.calculate_percentage() == 80


def test_calculate_cgpa():
    student = Student("Rahul", 101, [80, 90, 70])

    assert student.calculate_cgpa([8, 9, 7]) == 8


def test_calculate_percentage_empty_marks():
    student = Student("Rahul", 101, [])

    assert student.calculate_percentage() == 0


def test_calculate_cgpa_empty_grade_points():
    student = Student("Rahul", 101, [80, 90, 70])

    assert student.calculate_cgpa([]) == 0


def test_calculate_percentage_one_subject():
    student = Student("Rahul", 101, [92])

    assert student.calculate_percentage() == 92


def test_calculate_cgpa_multiple_subjects():
    student = Student("Rahul", 101, [80, 90, 70])

    assert student.calculate_cgpa([7.5, 8.5, 9.5]) == 8.5
