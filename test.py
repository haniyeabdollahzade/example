cs = [
    {"title": "Python",
     "teacher": "baqer marani"
     },
     {"title": "HTML",
      "teacher": "Ali mahdavi"
      }
]

class  User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        print(f"my fullname is {self.fname} {self.lname}")



class Student(User):
    def __init__(self, fname, lname, email):
        super().__init__(fname, lname)
        self.email = email
        self.courses = []


    def fullname(self):
        super().fullname()
        print(f"my email is {self.email}")  

    def printcourses(self):
        if self.courses:
            for course in self.courses:
                print(course.get("title"))
        else:
            print("This user no")        


class Teacher(User):
    def __init__(self, fname, lname, code):
        super().__init__(fname, lname)    
        self.code = code


    def fullname(self):
        super().fullname()
        print(f"my code is {self.code}")    


s1 = Student("haniye", "abdollahzadeh", "haniye@gmial.com")
s2 = Student("baqer", "marani", "baqer@gmail.com")

s1.fullname()
s1.courses.append(cs[0])
print(s1.courses)
s1.printcourses()

s2.printcourses()

