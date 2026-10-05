class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    @staticmethod
    def _average(values):
        if not values:
            return 0

        return sum(values) / len(values)

    def calculate_percentage(self):
        return self._average(self.marks)

    def calculate_cgpa(self, grade_points):
        return self._average(grade_points)
