import pandas as pd
import sys
from admin import Admin

df = pd.read_csv("course1.csv")
df1 = df[["major", "title"]]

file_path = "course1.csv"
df_course = pd.read_csv(file_path)
#course_lst = df_course.values.tolist()

class Course:

    def __init__(self, title, professor, course_id, unit, capacity, major, major_id, total_unit=None):
        self.title = title
        self.professor_name = professor
        self.course_id = course_id
        self.unit = unit
        self.capacity = capacity
        self.remain_capacity = capacity
        self.total_unit = total_unit
        self.major_id = major_id
        self.major = major

    def __sub__(self, other):
        self.remain_capacity = self.remain_capacity - other
        yield self
        if self.remain_capacity > 0:
            yield True

    def check(self):
        if self.remain_capacity > 0:
            return True

    # todo free this method
    def is_course_valid(self):
        pass

    def instance(self):
        pass

    def append_to_file(self, course_instance):
        for rows in df_course:
            rows[0] = self.title
            rows[1] = self.professor_name
            rows[2] = self.course_id
            rows[3] = self.unit
            rows[4] = self.capacity
            rows[5] = self.major
            rows[6] = self.major_id

    def __str__(self):
        return f"Title : {self.title} \n" \
               f"Professor : {self.professor_name} \n" \
               f"ID Course : {self.course_id} \n" \
               f"Unit : {self.unit} \n" \
               f"Capacity : {self.capacity} \n" \
               f"Remain Capacity: {self.remain_capacity} \n" \
               f"Total Unit: {self.total_unit}" \
               f"ID Major: {self.major_id}"


