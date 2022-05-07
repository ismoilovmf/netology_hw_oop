class Person:

    def __init__(self, name, surname, gender="unknown"):
        self.name = name
        self.surname = surname
        self.gender = gender


class Student(Person):

    def __init__(self, name, surname, gender="unknown"):
        super().__init__(name, surname, gender)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def s_grad(self):
        self.__sum = 0
        self.__count = 0
        for course in self.grades:
            self.__sum += sum(self.grades[course])
            self.__count += len(self.grades[course])
        if self.__count <= 0:
            return 0
        return self.__sum/self.__count

    def __str__(self):
        self.res = self.s_grad()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.res}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress) if self.courses_in_progress else '-'}\nЗавершенные курсы: {', '.join(self.finished_courses) if self.finished_courses else '-'}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.s_grad() > other.s_grad()


class Mentor(Person):

    def __init__(self, name, surname, gender="unknown"):
        super().__init__(name, surname, gender)
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, gender="unknown"):
        super().__init__(name, surname, gender)
        self.grades = {}

    def s_grad(self):
        self.__sum = 0
        self.__count = 0
        for s in self.courses_attached:
            self.__sum += sum(self.grades[s])
            self.__count += len(self.grades[s])
        return self.__sum / self.__count

    def __str__(self):
        res = self.s_grad()
        return f"Lecturer:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(res, 2)}"


class Reviewer(Mentor):
    def __init__(self, name, surname, gender="unknown"):
        super().__init__(name, surname, gender)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress or student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Reviewer:\nИмя: {self.name}\nФамилия: {self.surname}"


def s_grade(lst_s, course):
    sum_g = 0
    count_g = 0
    for s in lst_s:
        if course in s.grades:
            for c in s.grades:
                if c == course:
                    sum_g += sum(s.grades[c])
                    count_g += len(s.grades[c])
    return round(sum_g/count_g, 2)


student1 = Student('Student1', '1')
student2 = Student('Student2', '2')

student1.courses_in_progress += ['Python']
student2.finished_courses += ['Git']

lecturer1 = Lecturer("Lecturer1", "1")
lecturer2 = Lecturer("Lecturer2", "2")

lecturer1.courses_attached += ["Python"]
lecturer2.courses_attached += ["Git"]

reviwer1 = Reviewer('Reviewer1', '1')
reviwer2 = Reviewer('Reviewer2', '2')

reviwer1.courses_attached += ['Python']
reviwer2.courses_attached += ['Git']

reviwer1.rate_hw(student1, 'Python', 7.5)
reviwer2.rate_hw(student2, 'Git', 8.5)

student1.rate_lec(lecturer1, 'Python', 9.5)
student2.rate_lec(lecturer2, 'Git', 8.5)

print(student1.grades)
print(student2.grades)

print(lecturer1.grades)
print(lecturer2.grades)

print(reviwer1)
print(reviwer2)

print(lecturer1)
print(lecturer2)

print(student1)
print(student2)

print(student1.s_grad() > lecturer1.s_grad())
print(student2.s_grad() > lecturer2.s_grad())

print(s_grade([lecturer1, lecturer2], "Python"))
