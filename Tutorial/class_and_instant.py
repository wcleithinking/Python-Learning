# -*- coding: utf-8 -*-

class Student(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<=score <=100:
            self.__score = score
        else:
            raise ValueError('bad score!')

    def print_score(self):
        print('%s: %s' %(self.__name,self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=75:
            return 'B'
        elif self.__score >=60:
            return 'C'
        else:
            return 'D'


# test

bart = Student('Bart Simpson', 61)
bart.print_score()
print(bart.get_grade())
print(bart._Student__name)
bart.set_score(99)
bart.print_score()
bart.__name = 'newname'
print(bart.__name)
print(bart.get_name())
