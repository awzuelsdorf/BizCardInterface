# BizCardInterface

This is an interface for extracting someone's contact information from a
business card.

## Installation

This solution has been developed for Linux.

To install this solution on your system, either in a virtual environment
or not, you will need Python 3 and PIP installed.

To install this solution in a virtual environment, run these commands:

`virtualenv -p python3 .env`

`source .env/bin/activate`

`pip install -r requirements.txt`

`spacy download en_core_web_sm`

To install this solution outside of a virtual environment, run these commands:

`sudo -H pip install -r requirements.txt`

`sudo -H spacy download en_core_web_sm`

Please be patient with the `pip install` command and the `spacy download`
commands. Both can take several minutes to complete.

## Running the solution:

This solution is a command-line program. You can provide it with a business
card from a file or from the standard input.

Before running this solution, if you installed this solution in a virtual
environment, then make sure you have activated that environment before
running this script. 

To provide a business card from a file, run

`python BusinessCardDriver.py -f bizcard.txt`

where "bizcard.txt" is the path to your file.

To provide a business card from the standard input, run

`python BusinessCardDriver.py -i`

You will need to press Ctrl-d to let the program know
you are done entering your business card.

## Testing

To run the tests for this program, activate your virtual environment
(if you set one up earlier) and then run
 
`python -m unittest BusinessCardTest.py`

You should see four unit tests running and the word "OK" at the end.
