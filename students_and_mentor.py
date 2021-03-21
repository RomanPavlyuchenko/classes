from statistics import fmean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        temp = fmean([fmean(i) for i in self.grades.values()]) if self.grades.values() else 0
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {temp}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\n"
                f"Завершенные курсы: {self.finished_courses}")

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached\
                and [i for i in lecturer.courses_attached
                     if (i in self.finished_courses or i in self.courses_in_progress)]:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"

    def __lt__(self, other):  # <
        self_temp = fmean([fmean(i) for i in self.grades.values()]) if self.grades.values() else 0
        other_temp = fmean([fmean(i) for i in other.grades.values()]) if other.grades.values() else 0
        return self_temp < other_temp

    def __gt__(self, other):  # >
        return not self.__lt__(other)

    def __ne__(self, other):  # !=
        return not self.__eq__(other)

    def __eq__(self, other):  # ==
        self_temp = fmean([fmean(i) for i in self.grades.values()]) if self.grades.values() else 0
        other_temp = fmean([fmean(i) for i in other.grades.values()]) if other.grades.values() else 0
        return self_temp == other_temp

    def __le__(self, other):  # <=
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):  # >=
        return self.__gt__(other) or self.__eq__(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        temp = fmean([fmean(i) for i in self.grades.values()]) if self.grades.values() else 0
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n" 
                f"Средняя оценка за лекции: {temp}")

    def __lt__(self, other):  # <
        self_temp = fmean([fmean(i) for i in self.grades.values()]) if self.grades.values() else 0
        other_temp = fmean([fmean(i) for i in other.grades.values()]) if other.grades.values() else 0
        return self_temp < other_temp

    def __gt__(self, other):  # >
        return not self.__lt__(other)

    def __ne__(self, other):  # !=
        return not self.__eq__(other)

    def __eq__(self, other):  # ==
        self_temp = fmean([fmean(i) for i in self.grades.values()]) if self.grades.values() else 0
        other_temp = fmean([fmean(i) for i in other.grades.values()]) if other.grades.values() else 0
        return self_temp == other_temp

    def __le__(self, other):  # <=
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):  # >=
        return self.__gt__(other) or self.__eq__(other)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"


def students_grade_mean(students, course):
    temp = [fmean(i.grades[course]) for i in students if course in i.grades]
    return fmean(temp) if temp != [] else 0


def lecturers_grade_mean(lecturers, course):
    temp = [fmean(i.grades[course]) for i in lecturers if course in i.grades]
    print(temp)
    return fmean(temp) if temp != [] else 0


student1 = Student('Иван', 'Иванов', 'Male')
student1.finished_courses.append('Python')
student1.courses_in_progress.append('Git')
student2 = Student('Ольга', 'Ольгова', 'Female')
student2.courses_in_progress += ['Git', 'English']

lecturer1 = Lecturer('Андрей', 'Андреев')
lecturer1.courses_attached += ['Git', 'Python']
lecturer2 = Lecturer('Антон', 'Антонов')
lecturer2.courses_attached.append('English')

reviewer1 = Reviewer('Анна', 'Аннова')
reviewer1.courses_attached += ['Git', 'Python']
reviewer2 = Reviewer('Ксения', 'Ксеньева')
reviewer2.courses_attached += ['English']

student1.rate_lecturer(lecturer1, 'Git', 9)
student2.rate_lecturer(lecturer2, 'English',  9)

student2.rate_lecturer(lecturer1, 'Git', 1)

reviewer1.rate_hw(student1, 'Git', 3)
reviewer1.rate_hw(student2, 'Python', 4)

reviewer2.rate_hw(student1, 'English', 3)

print(student1 > student2)
print(student1 != student2)

print(lecturer1 > lecturer2)
print(lecturer1 != lecturer2)

print(lecturers_grade_mean([lecturer1, lecturer2], 'Git'))
print(students_grade_mean([student1, student2], 'Python'))

print(student1)
print(student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)
