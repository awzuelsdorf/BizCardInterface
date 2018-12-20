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
    def getMostLikelyPhone(cls, document):
        possiblePhones = re.findall(r"\s*(?:\+?(\d{1,3}))?[-.\s(]*(\d{3})[-.\s)]*(\d{3})[-.\s]*(\d{4})(?:\s*(ex|x|ext|extension)\s*(\d+))?\s*", document, flags=re.I)

        if len(possiblePhones) > 0:
            return "".join(possiblePhones[0])
        else:
            return None

    @classmethod
    def getContactInfo(cls, document):
        mostLikelyName = cls.getMostLikelyName(document)
        mostLikelyPhone = cls.getMostLikelyPhone(document)

        info = ContactInfo(mostLikelyName, mostLikelyPhone, "andrew@andrew.com")

        return info
