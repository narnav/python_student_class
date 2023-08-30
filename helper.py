from enum import Enum


class Actions(Enum):
    ADD_STUDENT =0
    PRINT_ALL_STUDENTS=1
    ADD_TEST =2
    AVG =3
    DISPLAY_SORTED_TESTS=4
    EXIT=5


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
        if len(self.test_lst) >0:
            total_grade = sum(test.grade for test in self.test_lst)
            average_grade = total_grade / len(self.test_lst)
            return average_grade

    def get_sorted_grades(self)-> list:
        return sorted([test.grade for test in self.test_lst])

    def __str__(self) -> str:
        return self.first_name + "," +self.last_name + " grade avg:" + str(self.get_avg())