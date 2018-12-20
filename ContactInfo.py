class ContactInfo(object):
    def __init__(self, name, phoneNumber, emailAddress):
        self.name = str(name)
        self.phoneNumber = str(phoneNumber)
        self.emailAddress = str(emailAddress)

    def getName(self):
        return str(self.name)

    def getPhoneNumber(self):
        return str(self.phoneNumber)

    def getEmailAddress(self):
        return str(self.emailAddress)

    def __str__(self):
        return "Name: {0}\nPhone: {1}\nEmail: {2}".format(self.name, self.phoneNumber, self.emailAddress)
