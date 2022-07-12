
class User:

    __UserIdGenerator = 0
    __contactIdGenerator = 1
    __contactDetailsIddGenerator = 1
    _ListOfUsers = []

    def __init__(self , userID , firstName , lastName , isAdmin ,  fullName):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.isAdmin = isAdmin
        self.isActive = True
        self.contacts = []
        self.fullName = fullName
        # self.__CONTACT = Contact()
    
    @staticmethod
    def createUser(firstName , lastName , isAdmin):
        if isAdmin:
            Admin.createAdmin( firstName , lastName)
        else:
            fullName = firstName + " " + lastName
            User.__UserIdGenerator += 1
            user = User(User.__UserIdGenerator , firstName , lastName , isAdmin , fullName)
            User.__ListOfUsers.append(user)
            return user

    def addContact(self , firstName , lastName , contactNumber , contactType , emailID):
        if self.isActive:
            contactDetails = ContactDetails(User.__contactDetailsIddGenerator , contactType , contactNumber , emailID)
            contact = Contact(User.__contactIdGenerator , firstName , lastName , True , contactDetails)
            self.contacts.append(contact)
            User.__contactDetailsIddGenerator += 1
            User.__contactIdGenerator += 1
        else:
            print("User not active")

    def getContactID(self , contactNumber):
        if self.isActive:
            for contact in self.contacts:
                if contact.contactDetails.contactNumber == contactNumber:
                    return contact.contactID
        else:
            print("User not active")

    def updateContactNumber(self , contactID , newNumber):
        if self.isActive:
            for contact in self.contacts:
                if contact.contactID == contactID:
                    contact.contactDetails.contactNumber = newNumber
        else:
            print("User not active")
            
    
    def updateFirstName(self , contactID , newName):
        if self.isActive:
            for contact in self.contacts:
                if contact.contactID == contactID:
                    contact.contactDetails.firstName = newName
        else:
            print("User not active")
    
    def updateLastName(self , contactID , newName):
        if self.isActive:
            for contact in self.contacts:
                if contact.contactID == contactID:
                    contact.contactDetails.lastName = newName
        else:
            print("User not active")

    def deleteContact(self , contactID):
        if self.isActive:
            for i in range(len(self.contacts)):
                if self.contacts[i].contactID == contactID:
                    self.contacts.pop(i)
                    break
        else:
            print("User not active")
    




class Contact:
    
    def __init__(self , contactID , firstName , lastName , isActive , contactDetails):
        self.contactID = contactID
        self.firstName = firstName
        self.lastName = lastName
        self.contactDetails = contactDetails


class ContactDetails:

    def __init__(self , contactDetailsID , contactType , contactNumber , emailID):
        self.contactDetailsID = contactDetailsID
        self.contactType = contactType
        self.contactNumber = contactNumber
        self.emailID = emailID
    
class Admin(User):

    def __init__(self , userID , firstName , lastName , fullName):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.isActive = True
        self.contacts = []
        self.fullName = fullName

    @staticmethod
    def createAdmin(firstName , lastName):
        userID = User.__UserIdGenerator
        User.__UserIdGenerator += 1
        fullName = firstName + " " + lastName
        return Admin(userID , firstName , lastName , fullName)

    def deleteUser(self , userID):
        for i in range(len(User._ListOfUsers)):
            if User._ListOfUsers[i].userID == userID:
                User._ListOfUsers[i].isActive = False
                break
    
    def deleteContact(self , userID , contactID):
        for user in User._ListOfUsers:
            if user.userID == userID:
                for i in range(len(user.contacts)):
                    if user.contacts[i].contactID == contactID:
                        user.contacts.pop(i)
                        break

    
    
