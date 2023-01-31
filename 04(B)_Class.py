


#Student Grade Displaying

class Student():
    def __init__(self,name="",mk=0):
        self.name=name
        self.marks=mk
    
    def grade(self):
        print("\n\tStudent Name = ",self.name.upper())
        if self.marks>60:
            print("\tGrade = A")
        elif self.marks>50:
            print("\tGrade = B")
        elif self.marks>=40:
            print("\tGrade = C")
        else:
            print("\tFail")
        
n=int(input("\tEnter the no. of student: "))
for i in range(n):
    Name=str(input("\tStudent name= "))
    Marks=int(input(f"\tMarks of {Name}="))
    s=Student(Name,Marks)
    s.grade()
    print("\t=====================\n")



"""
Output2:


        Enter the no. of student: 5
        Student name= vipul
        Marks of vipul=90

        Student Name =  VIPUL
        Grade = A
        =====================

        Student name= sahil
        Marks of sahil=58

        Student Name =  SAHIL
        Grade = B
        =====================

        Student name= abhi  
        Marks of abhi=45

        Student Name =  ABHI
        Grade = C
        =====================

        Student name= mrudul
        Marks of mrudul=85

        Student Name =  MRUDUL
        Grade = A
        =====================

        Student name= vishal
        Marks of vishal=35

        Student Name =  VISHAL
        Fail
        =====================

"""