# The fourth program implements (in a slightly simplified form) an algorithm used by European banks to specify account numbers. T
# he standard named IBAN (International Bank Account Number) provides a simple and fairly reliable method of
# validating the account numbers against simple typos that can occur during rewriting of the number e.g., from paper documents,
# like invoices or bills, into computers.
# You can find more details here: https://en.wikipedia.org/wiki/International_Bank_Account_Number
# An IBAN-compliant account number consists of:
# a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)
#
# two check digits used to perform the validity checks – fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;
#
# the actual account number (up to 30 alphanumeric characters – the length of that part depends on the country)
#
# The standard says that validation requires the following steps (according to Wikipedia):
#
#     (step 1) Check that the total IBAN length is correct as per the country (this program won’t do that, but you can modify the code to meet this requirement if you wish; note: you have to teach the code all the lengths used in Europe)
#     (step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
#     (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 .. Z = 35;
#     (step 4) Interpret the string as a decimal integer and compute the remainder of that number on division by 97; If the remainder is 1, the check digit test is passed and the IBAN might be valid.
#
# This is the code →
#
#     line 01: ask the user to enter the IBAN (the number can contain spaces, as they significantly improve number readability . . .
#     line 02: . . . but remove them immediately)
#     line 03: the entered IBAN must consist of digits and letters only – if it doesn’t . . .
#     line 04: . . . output the message;
#     line 05: the IBAN mustn’t be shorter than 15 characters (this is the shortest variant, used in Norway)
#     line 06: if it is shorter, the user is informed;
#     line 07: moreover, the IBAN cannot be longer than 31 characters (this is the longest variant, used in Malta)
#     line 08: if it is longer, make an announcement;
#     line 09: start the actual processing;
#     line 10: move the four initial characters to the number’s end, and convert all letters to upper case (step 02 of the algorithm)
#     line 11: this is the variable used to complete the number, created by replacing the letters with digits (according to the algorithm’s step 03)
#     line 12: iterate through the IBAN;
#     line 13: if the character is a digit . . .
#     line 14: . . . just copy it;
#     line 15: otherwise . . .
#     line 16: . . . convert it into two digits (note the way it’s done here)
#     line 17: the converted form of the IBAN is ready – make an integer out of it;
#     line 18: is the remainder of the division of iban2 by 97 equal to 1?
#     line 19: If yes, then success;
#     line 20: Otherwise . . .
#     line 21: . . .the number is invalid.
#
# Let’s add some test data (all these numbers are valid – you can invalidate them by changing any character).
#
#     British: GB72 HBZU 7006 7212 1253 00
#     French: FR76 30003 03620 00020216907 50
#     German: DE02100100100152517108
#
# If you are an EU resident, you can use you own account number for tests.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ', '')
if not iban.isalnum():
    print("Invalid characters inside IBAN - sorry!")
elif len(iban) < 15:
    print("IBAN too short")
elif len(iban) > 31:
    print("IBAN too long")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("Seems legit!")
    else:
        print("I don't think it's a valid IBAN, sorry")



