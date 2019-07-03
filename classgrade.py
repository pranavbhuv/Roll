
# ClassGradebook


class GradeBook:

    def  __init__(self):
        self.students = []
        self.teacher_name = "Tolain"
        self.class_name = "Python"
        self.start_time = "9:00"
        self.end_time = "3:00"

    def class_average(self):
        sum = 0
        for i in self.students:
            sum += i.grades
        return sum / len(self.students)

    def males(self):
        total_males = 0
        for x in range(len(self.students)):
            if self.students[x].gender == "male":
                total_males += 1
        print(total_males)

    def females(self):
        total_females = 0
        for x in range(len(self.students)):
            if self.students[x].gender == "female":
                total_females += 1
        print(total_females)

    def class_roster(self):
        for i in range(len(self.students)):
            print(self.students[i].name)

    def add_student(self, student):
        self.students.append(student)

    def bta(self, student_name, avg):
        for i in range(len(self.students)):
            if self.students[i].name == student_name:
                return self.students[i].grade > avg


class Student:
    def __init__(self, name, gender, grades, height):
        self.name = name
        self.gender = gender
        self.grades = grades
        self.height = height

    def student_height(self):
        print("Feet: ",int(self.height / 12), " Inches ", self.height % 12)


gb = GradeBook()

bill = Student("Bill", "male", 50, 72)
bob = Student("Bob", "male", 50, 80)
james = Student("James", "male", 90, 92)
will = Student("Will", "male", 80, 63)
karl = Student("Karl", "male", 70, 72)
erin = Student("Erin", "female", 100, 72)
kassie = Student("Kassie", "female", 20, 70)
selene = Student("Selene", "female", 40, 28)

gb.add_student(bill)
gb.add_student(bob)
gb.add_student(james)
gb.add_student(will)                                        
gb.add_student(karl)
gb.add_student(erin)
gb.add_student(kassie)
gb.add_student(selene)

rtp = True

while rtp == True:
    q = input("\n What do you want to do today? \n - Roster (r) \n - How many males? (m) \n - How many females? (f) \n - Teacher Name (tn) \n - Class Name (cn) \n - Start Time (st) \n - End Time (en) \n - Class Average (ca) \n - Add Student (as) \n - Is student doing better than average? (ba) \n - Student Height (sh) \n - Grade to Letter Calculator (kms)")
    print(q)
    if q == "r":
        print("\n")
        gb.class_roster()
    elif q == "m":
        print("\n We have this many males: \n")
        gb.males()
    elif q == "f":
        print("\n We have this many females: \n")
        gb.females()
    elif q == "tn":
        print("\n", "Our teacher is called: ", "\n", gb.teacher_name, "\n")
    elif q == "cn":
        print("\n", "Our class is called: ", "\n", gb.class_name, "\n")
    elif q == "st":
        print("\n", "Our class starts at: ", "\n", gb.start_time, "\n")
    elif q == "en":
        print("\n", "Our class ends at: ", "\n", gb.end_time, "\n")
    elif q == "ca":
        print("\n", "Our class average is: ", gb.class_average(), "\n")
    elif q == "as":
        print("\n")
        a = input("Type name of the student: ")
        b = input("What gender? ")
        c = input("What is his average?")
        d = input("What is its height in inches?")
        abcd = Student(a, b, c, d)
        gb.add_student(abcd)
    elif q == "ba":
        e = input("\n Please type in student name: ")
        gb.bta(e, gb.class_average())
    elif q == "sh":
         bill.student_height()
    else:
        f = int(input("\n Please type in the numerical grade to recieve a alphabetical grade! \n"))
        if f <= 50:
            print("\n You got an F, you failed!")
        elif 50 < f < 75:
            print("\n You got an C, better luck next time!")
        elif 75 < f < 89:
            print("\n You got an B, nice job!")
        elif f > 90:
            print("\n You got an A, well done!")
