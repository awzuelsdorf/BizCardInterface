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
        return "{0}\n{1}\n{2}\n".format(self.name, self.phoneNumber, self.emailAddress)
