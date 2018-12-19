from BusinessCardParser import BusinessCardParser
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Extracts name, phone number, and email address from output of Business Card OCR component.")

    parser.add_argument("-i", dest="inputFile", help="Path to business card text file. Omit to enter business card text from command line.",
required=False, default=None)

    args = parser.parse_args()

    document = None

    if args.inputFile is not None and not os.path.exists(args.inputFile):
        sys.stderr.write("ERROR: Could not find input file \"{0}\"\n".format(args.inputFile))
        sys.exit(1)
    elif args.inputFile is not None:
        inputFile = open(args.inputFile, 'r', encoding='utf-8')

        try:
            document = inputFile.read()
        finally:
            inputFile.close()
    else:
        print("Enter business card text. Press Ctrl-D on Mac or Linux (Ctrl-Z on Windows) to finish.")
        document = sys.stdin.read()

    contactInfo = BusinessCardParser.getContactInfo(document)

    print(str(contactInfo))

if __name__ == "__main__":
    main()
