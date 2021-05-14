import course
from login import User
from course import Course
from admin import Admin

print("please enter one item  \n"
      "1- login: \n"
      "2- signup:")
selection_item = int(input("your selection: "))
if selection_item == 1:
    User.login()
    # For Admin Role
    admin.define_course()
    title = input("Enter title:")
    professor = input("Enter professor: ")
    course_instance = Course(title, professor)
elif selection_item == 2:
    User.register()
else:
    print("Incorrect Enter")




