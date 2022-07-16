#----------------#oops_task#---------------09-07-2022

import logging as lg
lg.basicConfig(filename = "oops.log",format = "%(filename)s %(asctime)s %(message)s" ,level = lg.DEBUG)


#-------------- class 1----------------#
'''
class states_name:

    def __init__(self,name,population,capital,zone):
        self.name = name
        self.population = population
        self.capital = capital
        self.zone = zone

    def __repr__(self):
        return"  name: %s population: %s capital: %s zone: %s" %(self.name,self.population,self.capital,self.zone)
        lg.info("This is info message")


state1 = states_name("Maharashtra","16 Cr","Mumbai","West")
state2 = states_name("Assam", "6 Cr","Guwahati","North East")
state3 = states_name("Punjab","5 Cr","Chandigarh","North")
state4 = states_name("Karnataka","17 Cr","Bangalore","South")
state5 = states_name("Madhya Pradesh", "20 Cr","Bhopal","Central")

print(state1)
print(state2)
print(state3)
print(state4)
print(state5)

'''

#---------------class 2----------------#
'''
class player_name:
    
    def __init__(self,name,country,followers):
    
        self.name = name
        self.country = country
        self.followers = followers

    def __repr__(self):
        return" name: %s , Country: %s , Followers: %s" %(self.name,self.country,self.followers)
        
player1 = player_name("Virat Kohli","India",13.5)
player2 = player_name("Joss Buttler","England",1.5)
player3 = player_name("David Warner","Australia",1.2)

'''



#--------------class 3----------------#
"""
class students:

    def name():
        try:
            n = int(input("How many names you want to add"))
            for i in range(n):
                name = input("Enter your name")
                logging.info("%s input given",name)
            
        except Exception as e:
            print(str(e))
            students.name()

    def age():
        age = input("Enter age")
        

students.name()
"""


#-------------------class 4 multilevel inheritance----------------------#
"""
class internship:

   def student_details(self):
       try:
           name = input("Please enter name")
           category = input("Please select project category")
           lg.info("%(name)s enrolled for internship")
       except Exception as e:
            print(str(e))
class projects(internship):
    
    def python_projects(self):
        try:
            project = input("Select the python project")
            lg.info("%(project)s selected")
        except Exception as e:
            print(str(e))
            lg.error("Error in python_projrcts")

            
class summary(projects):
    def summ(self):
        try:
            print("This is list of all the projects and the students involved")
            lg.info("%(name)s selected %(project)s ")
        except Exception as e:
            print(str(e))
            lg.error("Error in summ")

i = summary()
i.student_details()
i.python_projects()
i.summ()
"""

#-------------------------------- class 5 multiple inheritance------------------#
"""
class comp_courses:

    def Data_Science(self):
        try:
            print("Following are the courses in Data Science")
            print("Data Analytics")
            print("FSDS")
            print("SQL")
            DS =input("Please select any of the above courses")
            lg.info(" Data Science COurse selected")
        except Exception as e:
            print(str(e))
            lg.error("Error from Data_Science")

    def Software(self):
        try:
            print("Following are the courses in Software Development")
            print(".net")
            print("C++")
            print("Java")
            soft =input("Please select any of the above courses")
            lg.info(" Software COurse selected")
        except Exception as e:
            print(str(e))
            lg.error("Erroe from Software")
            
        
class edu_courses:

    def std10(self):
        try:
            return "Following are the courses for Std 10"
            print("Science")
            print("Maths")
            print("English")
            s10 =input("Please select any of the above courses")
            lg.info(" Std 10 COurse selected")
        except Exception as e:
            print(str(e))
            lg.error("Error from Std10")
    
    def std9(self):
        try:
            return "Following are the courses for std 9"
            print("Hindi")
            print("Sanskrit")
            print("Arts")
            s9 = input("Please select any of the above courses")
        except Exception as e:
            print(str(e)))
            lg.error("Error from std9")
    
class course_summ(comp_courses,edu_courses):

    def summary_courses(self):
        return "Following are the courses selected by you %(s9)s,%(s10)s,%(DS)s,%(soft)s"


i = course_summ()
i.std10()
i.std9()
i.Software()
i.Data_Science()

"""

#----------------private-------------#
'''
class Account:
    __AccNO = 154878189874986
    def __bankacc(self):
        print("inside bankacc function ")

    def new(self):
        print("Private variable value",Account.__AccNO)
i = Account()
i.new()
i.__bankacc()

'''

#---------------protected---------------#
'''

class Account:
    _AccNO = 154878189874986
    def _bankacc(self):
        print("inside bankacc function ")

    def new(self):
        print("Private variable value",Account._AccNO)
i = Account()
i.new()
i._bankacc()

'''
#-------------Abstraction----------------#
'''
class calculator:

    def user_input():
        l = []
        try:
            numbers = int(input("Enter number of numbers"))
            for i in range(1,int(numbers)+1):
                data = int(input("Enter the numbers"))
                l.append(data)
            print(sum(l))
            lg.info(f"Input taken as {data}")
        except Exception as e:
            print(str(e))
            lg.error(f"Invalid Input {data}")

            
calculator.user_input()
'''

#-------------------Encapsulation----------------#
'''
class  HOF:

    def __init__(self):
        self.__students = "These are Hall of Famers"

    def students(self):
        print(self._HOF__students)

    def students_change(self,values):
        self.__students = values


i = HOF()
i.students()
#i.__students() = "New Hall of Famer"
i.students_change("Affiliates")
i.students()
'''
#-----------------Overriding------------------#

class Boss:

    def work(self):
        print("Get the work done from sub-ordinates")

    def arg(self):
        print("meet timeline")
        print(" Always Right")

class Employee:

    def arg(self):
        print("Never Wrong")

new = Boss()
new.arg()


#------------Polymorphism----------------#
'''
class students:

    def FSDS(self):
        print("Student Names and details")

class May_7:

    def FSDS(self):
        print("Class type of students")

def ineuron(a):
        a.FSDS()

i = students()
j = May_7()
ineuron(i)
ineuron(j)

'''









        
