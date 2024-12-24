class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        sum_grades = 0
        cnt_grades = 0
        for b in self.grades.values():
            sum_grades += sum(b)
            cnt_grades += len(b)
        if cnt_grades > 0:
            return sum_grades/cnt_grades 
        else:
            print('Студент еще не получал оценки')

    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\nКурсы в процессе изучения:{', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'

    def __eq__(self, others):
        return self._average_grade() == others._average_grade()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
   
 

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def _average_grade(self):
        sum_grades = 0
        cnt_grades = 0
        for b in self.grades.values():
            sum_grades += sum(b)
            cnt_grades += len(b)
        if cnt_grades > 0:
            return sum_grades/cnt_grades 
        else:
            print('Лектор еще не получал оценки')


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'

    def __eq__(self, others):
        return self._average_grade() == others._average_grade()

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
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    


student1 = Student('Егор', 'Петров', 'муж')
student1.courses_in_progress = ['Python', 'C#', 'Анализ данных']


student2 = Student('Кирилл', 'Петров', 'муж')
student2.courses_in_progress = ['Python', 'C#', 'Анализ данных']


lecturer1 = Lecturer('Алексей', 'Петросян')
lecturer1.courses_attached = ['Python', 'C#', 'Анализ данных']


lecturer2 = Lecturer('Сергей', 'Степаненко')
lecturer2.courses_attached = ['Python', 'C#', 'Анализ данных']


reviewer1 = Reviewer('Павел', 'Морозов')
reviewer1.courses_attached = ['Python', 'C#', 'Анализ данных']


reviewer2 = Reviewer('Кощей', 'Бессмертный')
reviewer2.courses_attached = ['Python', 'C#', 'Анализ данных']


student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer2, 'C#', 9)

student2.rate_lecturer(lecturer1, 'Python', 7)
student2.rate_lecturer(lecturer2, 'C#', 10)

reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student2, 'C#', 9)

reviewer2.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'C#', 5)

print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()
print(reviewer2)
print()
print(student1 == student2)
print(lecturer1 == lecturer2)

def students_course_rate(student_list, course):
    students_course_rate_sum = 0
    students_course_rate_cnt = 0
    for student in student_list:
        if isinstance(student, Student) and course in student.grades.keys():
           students_course_rate_sum += sum(student.grades[course])
           students_course_rate_cnt += len(student.grades[course])
        else:
            print(f'Оценки студенту {student.name} {student.surname} не выставлялись')
    return students_course_rate_sum/students_course_rate_cnt


def lecturer_course_rate(lecturer_list, course):
    lecturer_course_rate_sum = 0
    lecturer_course_rate_cnt = 0
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades.keys():
           lecturer_course_rate_sum += sum(lecturer.grades[course])
           lecturer_course_rate_cnt += len(lecturer.grades[course])
        else:
            print(f'Оценки лектору {lecturer.name} {lecturer.surname} не выставлялись')
    return lecturer_course_rate_sum/lecturer_course_rate_cnt

print(students_course_rate([student1, student2], 'Python'))
print(lecturer_course_rate([lecturer1, lecturer2], 'C#'))