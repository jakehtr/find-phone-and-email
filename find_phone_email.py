#! usr/bin/env python3

"""
phoneAndEmail.py - Finds phone numbers and email addresses from the clipboard.
"""

import pyperclip
import re


def find_matches():
    # find matches in clipboard text
    for groups in phone_regex.findall(text):
        matches.append(groups[0])
    for groups in email_regex.findall(text):
        matches.append(groups[0])


def get_results_from_clipboard():
    # first find the matches
    find_matches()
    # copy the results to the clipboard.
    if matches:
        all_matches = '\n'.join(matches)
        pyperclip.copy(all_matches)
        print('Copied to clipboard:\n{}'.format(all_matches))
    else:
        print('No phones numbers or email addresses found.')

if __name__ == '__main__':
    # create phone number regex
    phone_regex = re.compile(r'''(
        (\+44|0)                            # UK area code
        (\s\(0\)|\(0\))?                    # (0)
        (\s)?                               # separator
        (\d{2,4})                           # first 2-4 digits
        (\s)                                # separator
        (\d{4,8})                           # mid/last 4-8 digits
        (\s)?                               # separator
        (\d{4})?                            # last 4 digits
        )''', re.VERBOSE)

    # create email regex
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._-]+                     # username
        @                                   # @ symbol
        [a-zA-Z0-9-]+                       # domain name
        (\.[a-zA-Z]{2,4})                   # dot-something
        (\.[a-zA-Z]{2,4})?                  # extra dot-something
        )''', re.VERBOSE)

    text = '{}'.format(pyperclip.paste())
    matches = list()
    get_results_from_clipboard()
