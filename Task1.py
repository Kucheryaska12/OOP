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
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
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
    


