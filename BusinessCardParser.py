import re
import os
import spacy
from ContactInfo import ContactInfo

class BusinessCardParser(object):
    nat_lang_proc = spacy.load("en_core_web_sm")

    @classmethod
    def getContactInfo(cls, document):
        most_likely_name = None
        most_likely_name_diff = float("inf")

        for line in re.split(r"\n", document):
            entities = list(cls.nat_lang_proc(line).ents)

            for entity in entities:
                if entity.label_ == "PERSON":
                    entity_line_len_diff = len(line) - len(entity.text)

                    if entity_line_len_diff < most_likely_name_diff:
                        most_likely_name = str(entity.text)
                        most_likely_name_diff = entity_line_len_diff

        print("Most likely name: {0}, diff: {1}".format(most_likely_name, most_likely_name_diff))

        info = ContactInfo(most_likely_name, '12345678910', 'andrew@andrew.com')

        return info
