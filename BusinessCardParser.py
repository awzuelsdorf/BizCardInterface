import re
import os
import spacy
from ContactInfo import ContactInfo

class BusinessCardParser(object):
    natLangProc = spacy.load("en_core_web_sm")

    @classmethod
    def getMostLikelyName(cls, document):
        mostLikelyName = None
        mostLikelyNameDiff = float("inf")

        for line in re.split(r"\n", document):
            entities = list(cls.natLangProc(line).ents)

            for entity in entities:
                if entity.label_ == "PERSON":
                    entityLineLenDiff = len(line) - len(entity.text)

                    if entityLineLenDiff < mostLikelyNameDiff:
                        mostLikelyName = str(entity.text)
                        mostLikelyNameDiff = entityLineLenDiff

        return mostLikelyName

    @classmethod
    def getMostLikelyPhone(cls, document, extension=False):
        possiblePhones = list()

        if extension:
            regex = r"(?:\+?(\d{1,3}))?[-.\s(]*(\d{3})[-.\s)]*(\d{3})[-.\s]*(\d{4})(?:\s*(ex|x|ext|extension)\s*(\d+))?"
        else:
            regex = r"(?:\+?(\d{1,3}))?[-.\s(]*(\d{3})[-.\s)]*(\d{3})[-.\s]*(\d{4})?"

        for line in re.split(r"\n", document):
            #Skip fax machine numbers.
            if "f" not in line.lower():
                possiblePhones.extend(re.findall(regex, line, flags=re.I))

        if len(possiblePhones) > 0:
            return "".join(possiblePhones[0])
        else:
            return None

    @classmethod
    def getMostLikelyEmail(cls, document):
        possibleEmails = list()

        for line in re.split(r"\n", document):
            possibleEmails.extend(re.findall(r"\s*([^@\s]+@\S+)",
line, flags=re.I))

        if len(possibleEmails) > 0:
            return "".join(possibleEmails[0])
        else:
            return None

    @classmethod
    def getContactInfo(cls, document):
        mostLikelyName = cls.getMostLikelyName(document)
        mostLikelyPhone = cls.getMostLikelyPhone(document)
        mostLikelyEmail = cls.getMostLikelyEmail(document)

        info = ContactInfo(mostLikelyName, mostLikelyPhone, mostLikelyEmail)

        return info
