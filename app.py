from enum import Enum
import pickle


class Actions(Enum):
    ADD_STUDENT =0
    PRINT_ALL_STUDENTS=1
    ADD_TEST =2
    AVG =3
    EXIT=4


class Test:
    def __init__(self,test_name,grade) -> None:
        self.test_name=test_name
        self.grade=grade

 
class Student:
    def __init__(self,first_name,last_name) -> None:
        self.test_lst=[]
        self.first_name=first_name
        self.last_name=last_name

    def add_test (self,test_name,grade):
        self.test_lst.append(Test(test_name,grade))


    def get_avg(self):
        total_grade = sum(test.grade for test in self.test_lst)
        average_grade = total_grade / len(self.test_lst)
        return average_grade

    def __str__(self) -> str:
        return self.first_name + "," +self.last_name + " grade avg:" + str(self.get_avg())

students=[]
students_db='students.pkl'
DEBUG =0
def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# display a menu 4 the client
def menu():
    global students
    while(True):
        for act in Actions:
            print(f'{act.value}:  {act.name}')
        user_selection=Actions( int( input("select action")))
        if user_selection == Actions.EXIT:  return
        if user_selection == Actions.ADD_STUDENT:   students.append(Student(input("student first name?"),input("student last name?"))) 
        if user_selection == Actions.PRINT_ALL_STUDENTS:
            for stu in students: print(stu)
        if user_selection == Actions.ADD_TEST:  add_test()

def add_test():
    for index,stu in  enumerate(students):
        print(f'{index+1}: {stu.first_name}')
    selected_student= int(input(f'please selct a index ({1}-{len(students)})'))-1
    students[selected_student].add_test(input("test_name?"),int(input("grade")))


def test_data(Student, students):
    s1 = Student("maya","aaa")
    s1.add_test("english",34)
    students.append(s1)

if __name__ =="__main__":
    if DEBUG: test_data(Student, students)
    students = load_data(students_db)
    menu()
    save_data(students,students_db)