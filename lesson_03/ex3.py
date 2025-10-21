from student import Student
from course_group import CourseGroup

student = Student("Лев", "Толстой", 55, "Русская Литература")
classmate1 = Student ("Александр", "Пушкин", 46, "Русская Литература" )
classmate2 = Student("Борис", "Пастернак", 40, "Русская Литература")
classmate3 = Student("Антон", "Чехов", 45, "Русская Литература")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])
print(course_group)