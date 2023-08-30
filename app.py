from enum import Enum
import pickle

from helper import Actions, Student,Test


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
        if user_selection == Actions.DISPLAY_SORTED_TESTS:  get_student_sorted_tests()

def get_student_sorted_tests():
    for index,stu in  enumerate(students):
        print(f'{index+1}: {stu.first_name}')
    selected_student= int(input(f'please selct a index ({1}-{len(students)})'))-1
    print( students[selected_student].get_sorted_grades())


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