from BusinessCardParser import BusinessCardParser
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Extracts relevant contact info (name, phone number, and email address) from text of a business card.")

    parser.add_argument("-f", dest="inputFile",
help="Path to business card text file.", required=False, default=None)

    parser.add_argument("-i", dest="interactive",
help="Enter business card text interactively.", required=False,
default=False, action='store_true')

    args = parser.parse_args()

    if args.inputFile is None and not args.interactive:
        sys.stderr.write("ERROR: Need to provide either -i or -f arguments.\n")
        sys.exit(1)

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
        print("Enter business card text. Press Ctrl-d to finish.")
        document = sys.stdin.read()

    contactInfo = BusinessCardParser.getContactInfo(document)

    print("-------------------------")
    print("Contact Info:")
    print(str(contactInfo))
    print("-------------------------")

if __name__ == "__main__":
    main()
