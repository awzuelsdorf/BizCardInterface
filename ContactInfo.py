class ContactInfo(object):
    """
    A class representing a person's relevant contact information from a
    business card.
    """
    def __init__(self, name, phoneNumber, emailAddress):
        self.name = str(name)
        self.phoneNumber = str(phoneNumber)
        self.emailAddress = str(emailAddress)

    def getName(self):
        """
        Returns a copy of the string representing person's name.
        """
        return str(self.name)

    def getPhoneNumber(self):
        """
        Returns a copy of the string representing person's phone number.
        """
        return str(self.phoneNumber)

    def getEmailAddress(self):
        """
        Returns a copy of the string representing person's email address.
        """
        return str(self.emailAddress)

    def __str__(self):
        """
        Returns a string representation of this person's relevant contact
        information.
        """
        return "Name: {0}\nPhone: {1}\nEmail: {2}".format(self.name,
self.phoneNumber, self.emailAddress)
