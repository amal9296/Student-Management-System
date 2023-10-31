

# Department
class Department:
    # has a composition to school mamangement
    def __init__(self,DepartmentId,DepartmentName,InchargeName,MemberList):
        self.DepartmentId = DepartmentId
        self.DepartmentName = DepartmentName
        self.InchargeName = InchargeName
        self.MemberList = MemberList

    def DepartmentDetails(self):
        print('Department details') 
        print('--------------------------------------')
        print('DepartmentId:',self.DepartmentId) 
        print('DepartmentName:',self.DepartmentName)
        print('InchargeName:',self.InchargeName)
        print('MemberList:',self.MemberList)

# school management
class SchoolManagement:
    def __init__(self,SchoolName,Address,ContactNumber,MediumOfStudy,DepartmentId,DepartmentName,InchargeName,MemberList):
        self.SchoolName = SchoolName
        self.Address = Address
        self.ContactNumber = ContactNumber
        self.MediumOfStudy = MediumOfStudy
        # initialize the parametrs of department class
        self.DepartmentId = DepartmentId
        self.DepartmentName = DepartmentName
        self.InchargeName = InchargeName
        self.MemberList = MemberList
        # add composition from Department class
        self.DepartmentObject = Department(self.DepartmentId, self.DepartmentName,self.InchargeName,self.MemberList)


    def isOpen(self):
        print('open')
        # add time and day to filter the working days to check open or not    

    def SchoolDetails(self):
        print('school details')
        print('--------------------------------------')
        print('SchoolName:',self.SchoolName)
        print('Address:',self.Address)
        print('ContactNumber:',self.ContactNumber)
        print('MediumOfStudy:',self.MediumOfStudy)
        # composition class printing
        print(self.DepartmentObject.DepartmentDetails())


p = SchoolManagement(1,2,3,4,5,6,7,8) 
p.SchoolDetails()    
        