




# Student
class Student:
    def __init__(self,StudentId,StudentName,ClassId,Section,BusId):
        self.StudentId = StudentId
        self.StudentName = StudentName
        self.ClassId = ClassId
        self.Section = Section
        self.BusId = BusId

    def StudentDetails(self):
        print('------------------------------------')
        print('StudentId:',self.StudentId)
        print('StudentName:',self.StudentName)
        print('ClassId:',self.ClassId)
        print('Section:',self.Section)
        print('BusId:',self.BusId)

    def PayFees(self):
        print('feespayment of',self.StudentName,'of the class',self.ClassId,'of section',self.Section,'is completed')    


# primary student -- child of student
class PrimaryStudent(Student):
    return 'primary class student details'

class HigherSecondary(Student):
    print('higher secondary class student details')    

'''p = PrimaryStudent(1,2,3,4,5)    
p.StudentDetails()
q = HigherSecondary(11,12,13,14,15)
q.StudentDetails()'''
