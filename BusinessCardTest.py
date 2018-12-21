import unittest
from BusinessCardParser import BusinessCardParser

class BusinessCardTest(unittest.TestCase):
    def getFileText(self, filename):
        bizCardFile = open(filename, "r")
        bizCardFileText = bizCardFile.read()
        bizCardFile.close()
        return bizCardFileText

    def getContactInfo(self, filename):
        fileText = self.getFileText(filename)

        return BusinessCardParser.getContactInfo(fileText)

    def bizcardTestHelper(self, filename, realName, realEmail, realPhone):
        contactInfo = self.getContactInfo(filename)
        self.assertEqual(contactInfo.getName(), realName)
        self.assertEqual(contactInfo.getEmailAddress(), realEmail)
        self.assertEqual(contactInfo.getPhoneNumber(), realPhone)

    def test_bizcard1(self):
        self.bizcardTestHelper("bizcard1.txt", "Mike Smith",
"msmith@asymmetrik.com", "4105551234")

    def test_bizcard2(self):
        self.bizcardTestHelper("bizcard2.txt", "Lisa Huang",
"lisa.huang@foobartech.com", "4105551234")

    def test_bizcard3(self):
        self.bizcardTestHelper("bizcard3.txt", "Arthur Wilson",
"awilson@abctech.com", "17035551259")

    def test_bizcard4(self):
        self.bizcardTestHelper("bizcard4.txt", "Andrew Zuelsdorf",
"Andrew.Zuelsdorf@kirklawfirm.com", "14109675932")

    def test_bizcard5(self):
        self.bizcardTestHelper("bizcard5.txt", "Arthur Wilson",
"awilson@abctech.com", "17035551259")

if __name__ == "__main__":
    unittest.main()
