import csv
import pandas as pd
from login import User
from course import Course

file_path = "course1.csv"
df_course = pd.read_csv(file_path)
course_lst = df_course.values.tolist()

file_path1 = "student1.csv"
df_course = pd.read_csv(file_path1)
student_lst = df_course.values.tolist()


class Admin(User):
    def define_course(self, course_name, professor, course_id, unit, capacity, major, major_id):
        course_instance = Course(course_name, professor, course_id, unit, capacity, major, major_id)

        # Course.append_to_file(course_instance)

    def see_lst_students(self, student_lst):
        for student in student_lst:
            if student.major_code == self.major_code:
                student_lst.add([student.student_name, student.student_lastname,
                                 student.student_number, student.major, student.major_code,
                                 student.username, student.password])
        return student_lst

    def select_student(self, student_num):
        if student_num == self.student_number:
            return True


Admin.define_course("Maths", "profname", "id", "3", "15", "computer science", "1")